# Kepco tariff calculation
from datetime import datetime, timedelta, time

# Low voltage / High voltage
LV = 0
HV = 1
# Base fee / Usage-based fee
BASIC = 0
USAGE = 1
# Customer Choices per usage pattern
Type1 = 0
Type2 = 1
Type3 = 2
Type4 = 3
# time range during day Low load time, High load time, Peak load time 
LLOAD = 0
HLOAD = 1
PLOAD = 2
# Seasonal charge, Summer, Winter and the rest
SUMMER = 0
OTHER = 1
WINTER = 2

price_table = [
    [2390,
        [
            [
                [76.5, 66.0, 91.2], [142.8, 77.8, 123.7], [184.1, 82.7, 152.6]
            ],
            [
                [63.7, 66.0, 86.4], [120.6, 77.8, 107.3], [251.4, 82.7, 207.6]
            ],
            [
                [70.7, 66.0, 96.1], [119.2, 77.8, 106.0], [216.6, 82.7, 179.0]
            ],
            [
                [152.6, 77.8, 135.5], [152.6, 77.8, 135.5], [152.6, 77.8, 135.5]
            ]
        ]
    ],
    [2580,
        [
            [
                [70.4, 60.8, 80.0], [110.5, 71.6, 99.0], [131.8, 75.5, 113.0]
            ],
            [
                [58.8, 60.8, 75.8], [93.6, 71.6, 86.1], [179.2, 75.5, 153.0]
            ],
            [
                [65.1, 60.8, 84.2], [92.5, 71.6, 85.1], [154.6, 75.5, 132.2]
            ],
            [
                [118.0, 71.6, 108.3], [118.0, 71.6, 108.3], [118.0, 71.6, 108.3]
            ]
        ]
    ]
]

def calculate_price(start_time, end_time, energy):

  # Convert the start and end times to datetime objects
  start_datetime = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
  end_datetime = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')

  # Average energy for the duration
  total_hours = (end_datetime - start_datetime) / timedelta(hours=1)
  average_energy = energy / total_hours
  print("전체 {}시간 동안 평균 {}kW로 충전: 매출 {}원".format(total_hours, average_energy, energy * 180))

  if average_energy < 3.5:
    cat_charger = 3
  else:
    cat_charger = 7

  # Base fee calculation
  base_fee = price_table[HV][BASIC] * cat_charger / (30 * 24 * 0.1) * total_hours
  
  # Calculate the total price for the given period
  total_price = 0
  start_end_flag = 0
  current_datetime = start_datetime
  while current_datetime < end_datetime:
    # Calculate the price for the current date and time
    if current_datetime == start_datetime:
      start_end_flag = 1
    elif end_datetime - current_datetime < timedelta(seconds=3600):
      current_datetime = end_datetime
      start_end_flag = 2
    else:
      start_end_flag = 0
    date_obj = current_datetime.date()
    time_obj = current_datetime.time()
    print("{} {} 부터 다음 구간까지".format(date_obj, time_obj))
    price = calculate_price_for_date_and_time(date_obj, time_obj, start_end_flag, average_energy)
    total_price += price

    # Move to the next hour
    if start_end_flag == 1:
      start_second = current_datetime.time().minute * 60 + current_datetime.time().second
      current_datetime += timedelta(seconds=(3600-start_second))
    elif start_end_flag == 0:
      current_datetime += timedelta(hours=1)

  return total_price, base_fee

def calculate_price_for_date_and_time(date_obj, time_obj, start_end_flag, average_energy):
  # Determine the season based on the month of the date
  month = date_obj.month
  if month in (11, 12, 1, 2):
    season = WINTER
  elif month in (6, 7, 8):
    season = SUMMER
  else:
    season = OTHER

  if season == WINTER:
    # Determine the time range based on the time
    if time_obj >= time(22, 00, 00) or time_obj < time(8, 00, 00):
      time_range = LLOAD
    elif time_obj >= time(8, 00, 00) and time_obj < time(9, 00, 00):
      time_range = HLOAD
    elif time_obj >= time(12, 00, 00) and time_obj < time(16, 00, 00):
      time_range = HLOAD
    elif time_obj >= time(19, 00, 00) and time_obj < time(22, 00, 00):
      time_range = HLOAD
    else:
      time_range = PLOAD
  else:
    # Determine the time range based on the time
    if time_obj > time(22, 00, 00) or time_obj <= time(8, 00, 00):
      time_range = LLOAD
    elif time_obj > time(8, 00, 00) and time_obj <= time(11, 00, 00):
      time_range = HLOAD
    elif time_obj > time(12, 00, 00) and time_obj <= time(13, 00, 00):
      time_range = HLOAD
    elif time_obj > time(18, 00, 00) and time_obj <= time(22, 00, 00):
      time_range = HLOAD
    else:
      time_range = PLOAD

  # Calculate the actual usage rate for start and end time range.
  if start_end_flag == 1:
    actual_rate = (60 - time_obj.minute)/60
  elif start_end_flag == 2:
    actual_rate = time_obj.minute / 60
  else:
    actual_rate = 1

  # Calculate the price based on season and time range
  price = price_table[HV][USAGE][Type1][time_range][season]

  actual_price = average_energy * price * actual_rate
  # base_fee = price_table[HV][BASIC] * cat_charger / (30 * 24 * 0.1) * total_hours
  print("충전금액은 %.2f" % actual_price)
  return actual_price

# 시간 정보
# start_time = "2022-12-10T13:30:01.634615"
# end_time = "2022-12-10T15:00:00.634615"
start_time = "2022-10-31T22:10:00Z"
end_time = "2022-11-01T02:10:00Z"
energy = 28

# starttime_obj = datetime.fromisoformat(starttime)
# endtime_obj = datetime.fromisoformat(endtime)

total_price, base_fee = calculate_price(start_time, end_time, energy)
print("기본요금 {:.2f} 이용요금 {:.2f} 포함 매출원가 {:.2f}".format(base_fee, total_price, base_fee + total_price))