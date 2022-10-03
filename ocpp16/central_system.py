import asyncio
import logging
from datetime import datetime
import requests
import json
import uuid

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from cardinfo.models import Cardinfo
from evcharger.models import Evcharger
from variables.models import Variables
from clients.models import Clients

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('ocpp')

global Job_List

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

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "idTagInfo" : { 'parentIdTag': id_tag,
                'status': status }
          }]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'BootNotification':
        logging.info('========== Got a Boot Notification ==========')

        cpnumber = ocpp_req['cpnumber']
        queryset = Evcharger.objects.filter(cpnumber=cpnumber).values()
        if queryset.count() == 0:
          status = "Rejected"   # need to implement "Pending"
        else:
          status = "Accepted"

        queryset = Variables.objects.filter(group="group0").values()
        if queryset.count() == 0:
          interval = 480
        else:
          interval = queryset[0]['interval']        

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "currentTime":"2022-08-06T03:44:37.668365",
            "interval": interval,
            "status": status
          }]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'Heartbeat':
        logging.info('========== Got a Heartbeat ==========') 

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "currentTime":datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + "Z",
          }]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'StatusNotification':
        logging.info('========== Got a StatusNotification Req ==========')

        cpnumber = ocpp_req['cpnumber']
        queryset = Evcharger.objects.filter(cpnumber=cpnumber).values()
        if queryset.count() == 0:
          Print("OCPP Message Error: CP is not available")
        else:
          if ocpp_req['msg_content']['connectorId'] == 0:
            Evcharger.objects.filter(cpnumber=cpnumber).update(connector_id_0_status=ocpp_req['msg_content']['status'])
          if ocpp_req['msg_content']['connectorId'] == 1:
            Evcharger.objects.filter(cpnumber=cpnumber).update(connector_id_1_status=ocpp_req['msg_content']['status'])
          else:
            pass

        ocpp_conf = [3, ocpp_req['connection_id'], {}]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'DataTransfer':
        logging.info('========== Got a DataTransfer ==========')
        if ocpp_req['msg_content']['messageId'] == "uvStartCardRegMode":
          targetcp = ocpp_req['msg_content']['data']['targetcp']
          queryset = Clients.objects.filter(cpnumber=targetcp).values()
          Clients.objects.filter(cpnumber=ocpp_req['cpnumber']).update(connection_id=ocpp_req['connection_id'])
          channel_name = queryset[0]['channel_name']
          message = [2, ocpp_req['connection_id'], ocpp_req['msg_name'], ocpp_req['msg_content']]
          print('OCPP Conf in central_system: Send To {} : {}'.format(targetcp, message))          
          channel_layer = get_channel_layer()
          async_to_sync(channel_layer.send)(channel_name, {
            "type" : "ocpp16_message",
            "message" : message
          }) 

        elif ocpp_req['msg_content']['messageId'] == "uvCardRegStatus":
          if ocpp_req['msg_content']['data']['status'] == "CardAuthMode":
            ocpp_conf = [3, ocpp_req['connection_id'],
            {
              "status":"Accepted"
            }]
            return ocpp_conf
        elif ocpp_req['msg_content']['messageId'] == "uvCardReg":
          print('Cardtag = ', ocpp_req['msg_content'])
          Cardinfo.objects.filter(userid=ocpp_req['msg_content']['data']['memberId'], cardstatus="처리중").update(cardtag=ocpp_req['msg_content']['data']['token'], cardstatus='배포됨')
          ocpp_conf = [3, ocpp_req['connection_id'],
          {
          "status":"Accepted"
          }]
          return ocpp_conf

    elif ocpp_req['msg_name'] == 'DiagnosticsStatusNotification':
        logging.info('========== Got a Diagnostics Status Notification ==========')
        return call_result.DiagnosticsStatusNotification()

    elif ocpp_req['msg_name'] == 'FirmwareStatusNotification':
        logging.info('========== Got a Firmware Status Notification ==========')
        return call_result.FirmwareStatusNotification()

    elif ocpp_req['msg_name'] == 'MeterValues':
        logging.info('========== Got a MeterValue Req ==========')
        ocpp_conf = [3, ocpp_req['connection_id'],{}]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'StartTransaction':
        logging.info('========== Got a StartTransaction Req ==========')

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "transactionId" : ocpp_req['connection_id'],
            "idTagInfo" : {'parentIdTag': ocpp_req['msg_content']['idTag'],
                'status': 'Accepted' }
          }]
        return ocpp_conf

    elif ocpp_req['msg_name'] == 'StopTransaction':
        logging.info('========== Got a StopTransaction Req ==========')

        # [2, '1901019473', 'StopTransaction', 
        # {'idTag': '0000000000150049', 'meterStop': 182, 'reason': 'Local', 'timestamp': '2022-08-06T03:45:45Z', 'transactionId': -1, 
        #  'transactionData': [
        #     {'timestamp': '2022-08-06T03:45:45Z', 'sampledValue': [
        #         {'value': '0.00', 'context': 'Sample.Periodic', 'format': 'Raw', 'measurand': 'Energy.Active.Import.Register', 'unit': 'Wh'}
        #         ]
        #     }
        #  ]
        # }]

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "idTagInfo" : {'parentIdTag': ocpp_req['msg_content']['idTag'],
                'status': 'Accepted' }
          }]
        return ocpp_conf

    else:
      pass


def message_transfer(ocpp_req):
  print(dir(message_transfer))
  if ocpp_req['msg_direction'] == 2:
    logging.info('========== Send a DataTransfer ==========')
    if ocpp_req['msg_content']['messageId'] == "uvStartCardRegMode":
      queryset = Clients.objects.filter(cpnumber=ocpp_req['cpnumber']).values()
      Clients.objects.filter(cpnumber=ocpp_req['cpnumber']).update(connection_id=ocpp_req['connection_id'])
      channel_name = queryset[0]['channel_name']
      message = [2, ocpp_req['connection_id'], ocpp_req['msg_name'], ocpp_req['msg_content']]
      print('OCPP Conf : Send To {} : {}'.format(ocpp_req['cpnumber'], message))          
      channel_layer = get_channel_layer()
      conf = async_to_sync(channel_layer.send)(channel_name, {
        "type" : "ocpp16_message",
        "message" : message
      }) 
  elif ocpp_req['msg_direction'] == 3:
    logging.info('========== Got a DataTransfer Conf ==========')
    ocpp_conf = [3, ocpp_req['connection_id'], ocpp_req['msg_content']]
    return ocpp_conf


def ocpp_conf_from_cp(cpnumber, ocpp_conf):

  queryset = Clients.objects.filter(cpnumber=cpnumber).values()
  if ocpp_conf['connection_id'] == queryset[0]['connection_id']:
    ocpp_conf['msg_name'] = queryset[0]['channel_status']
  
  if ocpp_conf['msg_name'] == 'Reset':
    print("===================================")
    print("Reset is accepted")
    print("===================================")

  elif ocpp_conf['msg_name'] == 'ChangeAvailability':
    print("===================================")
    print("ChangeAvailability is accepted")
    print("===================================")

  elif ocpp_conf['msg_name'] == 'ChangeConfiguration':
    print("===================================")
    print("ChangeConfiguration is accepted")
    print("===================================")

  elif ocpp_conf['msg_name'] == 'ClearCache':
      print("===================================")
      print("ClearCache is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'DataTransfer':
      print("===================================")
      print("DataTransfer is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'GetConfiguration':
      print("===================================")
      print("GetConfiguration is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'RemoteStartTransaction':
      print("===================================")
      print("RemoteStartTransaction is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'RemoteStopTransaction':
      print("===================================")
      print("RemoteStopTransaction is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'TriggerMessage':
      print("===================================")
      print("TriggerMessage is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'GetDiagnostics':
      print("===================================")
      print("GetDiagnostics is accepted")
      print("===================================")

  elif ocpp_conf['msg_name'] == 'UpdateFirmware':
      print("===================================")
      print("UpdateFirmware is accepted")
      print("===================================")

  else:
    print("{} message is confirmed".format(ocpp_conf['msg_name']))


    
