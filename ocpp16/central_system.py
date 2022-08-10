import asyncio
import logging
from datetime import datetime
import requests
import json

from cardinfo.models import Cardinfo

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('ocpp')

CP_CONNECTIONS = {}

def ocpp_request(ocpp_req):
    unique_id = None  

    if ocpp_req['msg_name'] == 'Authorize':
        logging.info('========== Got an Authorize Req ==========')
        id_tag = ocpp_req['msg_content']['idTag']

        queryset = Cardinfo.objects.filter(cardtag=id_tag).values()
        if queryset.count() == 0:
          status = "Invalid"
        else:
          status = "Accepted"
        print('Authorization status = ', status)
        
        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "idTagInfo" : { 'parentIdTag': id_tag,
                'status': status }
          }]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'BootNotification':
        logging.info('========== Got a Boot Notification ==========')
        # cpname = self.id.split('/')[-1]
        # CP_CONNECTIONS[cpname] = self._connection
        # print(CP_CONNECTIONS)
        # print('unique_id:', self.unique_id)
        # print(dir(self))
        # msg = {
        #     "msg_direction": 2,
        #     "msg_name": "BootNotification",
        #     "msg_content": {
        #         "charge_point_model": charge_point_model,
        #         "charge_point_vendor": charge_point_vendor
        #     },
        #     "connection_id": self.unique_id,
        #     "cpname": cpname, 
        # }
        # result = datalog_to_database(msg)
        # res = result.json()
        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "currentTime":"2022-08-06T03:44:37.668365",
            "interval":180,
            "status":"Accepted"
          }]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'Heartbeat':
        logging.info('========== Got a Heartbeat ==========') 

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "currentTime":datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + "Z",
          }]
        return ocpp_conf

    # def on_status_notification(self, connector_id: int, error_code: str, status: str, **kwargs):
    elif ocpp_req['msg_name'] == 'StatusNotification':
        logging.info('========== Got a StatusNotification Req ==========')

        ocpp_conf = [3, ocpp_req['connection_id'], {}]
        return ocpp_conf

    else:
      pass
    # @on(Action.DataTransfer)
    # def on_data_transfer(self, vendor_id: str, message_id: str, **kwargs):
    #     logging.info('========== Got a DataTransfer ==========')
    #     cpname = self.id.split('/')[-1]
    #     msg = {
    #         "msg_direction": 2,
    #         "msg_name": "DataTransfer",
    #         "msg_content": {
    #             "vendor_id": vendor_id,
    #             "message_id": message_id,
    #             "data": kwargs['data']
    #         },
    #         "connection_id": self.unique_id,
    #         "cpname": cpname, 
    #     }
    #     result = datalog_to_database(msg)
    #     res = result.json()

    #     if message_id == "StartCardRegMode":
    #         cp = ChargePoint(cpname, CP_CONNECTIONS[cpname])
    #         cp.data_transfer(vendor_id, msg)
            # Redirect data trasfer to CP100
            # request = call.DataTransferPayload(
            #     vendor_id =vendor_id,
            #     message_id = message_id,
            #     data = kwargs['data'],
            # )

            # response = msg_to_cp(msg)

            # if response.id_tag_info['status'] == "Accepted":
            # print('response =  ',  dir(response))
        # print('response.status = %s' % response.status)
        # print('payload = %s' % response.payload)

        # if response.payload["status"] == "Accepted":
        #     print("===================================")
            # print("Card Registration  is accepted.")
        #     print("===================================")
        
    #     return call_result.DataTransferPayload(
    #         status=RegistrationStatus.accepted
    #     )

    # @on(Action.DiagnosticsStatusNotification)
    # def on_diagnostics_status_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
    #     logging.info('========== Got a Diagnostics Status Notification ==========')
    #     return call_result.DiagnosticsStatusNotification()

    # @on(Action.FirmwareStatusNotification)
    # def on_firmware_status_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
    #     logging.info('========== Got a Firmware Status Notification ==========')
    #     return call_result.FirmwareStatusNotification()



    # @on(Action.MeterValues)
    # def on_metervalues(self, connector_id: int, meter_value: str, transaction_id: int):
    #     logging.info('========== Got a MeterValue Req ==========')
    #     return call_result.MeterValuesPayload()

    # @on(Action.StartTransaction)
    # def on_start_transaction(self, connector_id: int, id_tag: str, meter_start: int, timestamp: str, **kwargs):
    #     logging.info('========== Got a StartTransaction Req ==========')
    #     return call_result.StartTransactionPayload(
    #         transaction_id=1,
    #         id_tag_info={ 'parent_id_tag': id_tag,
    #             'status': RegistrationStatus.accepted }
    #     )

    # @on(Action.StatusNotification)
    # def on_status_notification(self, connector_id: int, error_code: str, status: str, **kwargs):
    #     logging.info('========== Got a StatusNotification Req ==========')
    #     return call_result.StatusNotificationPayload()

    # @on(Action.StopTransaction)
    # def on_stop_transaction(self, id_tag: str, meter_stop: int, timestamp: str, transaction_id: int):
    #     logging.info('========== Got a StopTransaction Req ==========')
    #     return call_result.StopTransactionPayload(
    #         id_tag_info={ 'parent_id_tag': id_tag,
    #             'status': RegistrationStatus.accepted }
    #     )

    # async def cancel_reservation(self):
    #     request = call.CancelReservationPayload(
    #         revervation_id = 1
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Calcel Reservation is accepted.")
    #         print("===================================")

    # async def change_availability(self):
    #     request = call.ChangeAvailabilityPayload(
    #         connector_id = 1,
    #         type = 'AvailabilityType'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Change Availability is accepted.")
    #         print("===================================")

    # async def change_configuration(self):
    #     request = call.ChangeConfigurationPayload(
    #         key = 'str', 
    #         value = 'Any'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Change Configuration is accepted.")
    #         print("===================================")

    # async def clear_cache(self):
    #     request = call.ClearCachePayload()

    #     response = await self.call(request)
    #     print("===================================")
    #     print("Clear Cache transferred.....")
    #     print("===================================")

    # async def clear_charging_profile(self):
    #     request = call.ClearChargingProfilePayload(
    #         # options: id, connector_id, charging_profile_purpose, stack_level
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Clear Change Profile is accepted.")
    #         print("===================================")

    # async def data_transfer(self, vendor_id: str, message_id: str, **kwargs):
    #     request = call.DataTransferPayload(
    #         vendor_id ="gresystem",   
    #         message_id = "StartCardRegMode",
    #         data = {'user_id': 'jeongsoogh1'},
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Data Transfer is accepted.")
    #         print("===================================")



    # async def get_composite_schedule(self):
    #     request = call.GetCompositeSchedulePayload(
    #         connector_id = 1,
    #         duration = 60
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Get Composite Schedule is accepted.")
    #         print("===================================")

    # async def get_configuration(self):
    #     request = call.GetConfigurationPayload(
    #         # options : key
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Get Configuration is accepted.")
    #         print("===================================")

    # async def get_diagnostics(self):
    #     request = call.GetDiagnosticsPayload(
    #         location = 'str'
    #         # options : retries, retry_interval, start_time, stop_time
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Get Diagnostics is accepted.")
    #         print("===================================")

    # async def get_local_list_version(self):
    #     request = call.GetLocalListVersionPayload()

    #     response = await self.call(request)
    #     print("===================================")
    #     print("Get Local List Version transferred.....")
    #     print("===================================")

    # async def remote_start_transaction(self):
    #     request = call.RemoteStartTransactionPayload(
    #         id_tag = 'str'
    #         # options : connector_id, changing_profile
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Remote Start Transaction is accepted.")
    #         print("===================================")

    # async def remote_stop_transaction(self):
    #     request = call.RemoteStopTransactionPayload(
    #         transaction_id = 1
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Remote Stop Transaction is accepted.")
    #         print("===================================")

    # async def reserve_now(self):
    #     request = call.ReserveNowPayload(
    #         connector_id = 1,
    #         expiry_date = "datatime str",
    #         id_tag = 'str',
    #         reservation_id = 1, 
    #         # options: parent_id_tag
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Reserve Now is accepted.")
    #         print("===================================")

    # async def reset(self):
    #     request = call.ResetPayload(
    #         type = 'Reset Type'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Reset is accepted.")
    #         print("===================================")

    # async def send_local_list(self):
    #     request = call.SendLocalListPayload(
    #         type = 'Reset Type'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Send Local List is accepted.")
    #         print("===================================")

    # async def set_charging_profile(self):
    #     request = call.SetChargingProfilePayload(
    #         connector_id = 1,
    #         cs_charging_profiles = 'Dict'
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Set Charging Profile is accepted.")
    #         print("===================================")

    # async def trigger_message(self):
    #     request = call.TriggerMessagePayload(
    #         requested_message = 'MessageTrigger'
    #         # connector_id: Optional[int] = None
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Trigger Message is accepted.")
    #         print("===================================")

    # async def unlock_connector(self):
    #     request = call.UnlockConnectorPayload(
    #         connector_id = 1
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Unlock Connector is accepted.")
    #         print("===================================")

    # async def update_firmware(self):
    #     request = call.UpdateFirmwarePayload(
    #         location = 'str',
    #         retrieve_date = 'datetime str'
    #         # options: retries: int, retry_interval: int
    #     )

    #     response = await self.call(request)
    #     if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #         print("===================================")
    #         print("Update Firmware is accepted.")
    #         print("===================================")