import asyncio
import websockets
import json
import uuid

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from clients.models import Clients
from .consumers import Ocpp16Consumer

def get_cardtag(cpnumber, userid):
  vendorId = "gresystem"
  messageId = "uvStartCardRegMode"
  msg = {
    "memberId":userid,
    "targetcp":cpnumber
  }
  ocpp_req = {
        "msg_direction" : 2,
        "connection_id" : str(uuid.uuid4()),
        "msg_name": "DataTransfer",
        "msg_content": {'vendorId':vendorId,'messageId':messageId,'data': msg},
      }

  consumer = Ocpp16Consumer()
  message = [2, ocpp_req['connection_id'], ocpp_req['msg_name'], ocpp_req['msg_content']]
  print('data transfer req: ', message)
  queryset = Clients.objects.filter(cpnumber=cpnumber).values()
  channel_name = queryset[0]['channel_name']

  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.send)(
    channel_name,
    {
      'type':'ocpp16_message',
      'message':message 
    }
  )

  