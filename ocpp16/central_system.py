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

    # def on_status_notification(self, connector_id: int, error_code: str, status: str, **kwargs):
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

    # def on_data_transfer(self, vendor_id: str, message_id: str, **kwargs):
    elif ocpp_req['msg_name'] == 'DataTransfer':
        logging.info('========== Got a DataTransfer ==========')
        if ocpp_req['msg_direction'] == 2:
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
        elif ocpp_req['msg_direction'] == 3:
          queryset = Clients.objects.filter(connection_id=ocpp_req['connection_id']).values()
          connection_id = queryset[0]['connection_id']
          if ocpp_req['connection_id'] == connection_id:
            ocpp_conf = [3, ocpp_req['connection_id'], ocpp_req['msg_content']]
            return ocpp_conf

    # def on_diagnostics_status_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
    elif ocpp_req['msg_name'] == 'DiagnosticsStatusNotification':
        logging.info('========== Got a Diagnostics Status Notification ==========')
        return call_result.DiagnosticsStatusNotification()

    # def on_firmware_status_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
    elif ocpp_req['msg_name'] == 'FirmwareStatusNotification':
        logging.info('========== Got a Firmware Status Notification ==========')
        return call_result.FirmwareStatusNotification()

    # def on_metervalues(self, connector_id: int, meter_value: str, transaction_id: int):
    # elif ocpp_req['msg_name'] == 'MeterValues' or 'MeterValue':
    elif ocpp_req['msg_name'] == 'MeterValues':
        logging.info('========== Got a MeterValue Req ==========')
        ocpp_conf = [3, ocpp_req['connection_id'],{}]
        return ocpp_conf

    # def on_start_transaction(self, connector_id: int, id_tag: str, meter_start: int, timestamp: str, **kwargs):
    elif ocpp_req['msg_name'] == 'StartTransaction':
        logging.info('========== Got a StartTransaction Req ==========')

        ocpp_conf = [3, ocpp_req['connection_id'],
          {
            "transactionId" : ocpp_req['connection_id'],
            "idTagInfo" : {'parentIdTag': ocpp_req['msg_content']['idTag'],
                'status': 'Accepted' }
          }]
        return ocpp_conf

    # def on_stop_transaction(self, id_tag: str, meter_stop: int, timestamp: str, transaction_id: int):
    elif ocpp_req['msg_name'] == 'StopTransaction':
        logging.info('========== Got a StopTransaction Req ==========')
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

    # response = self.call(request)
    # if response.id_tag_info['status'] == RegistrationStatus.accepted:
    #     print("===================================")
    #     print("Data Transfer is accepted.")
    #     print("===================================")

