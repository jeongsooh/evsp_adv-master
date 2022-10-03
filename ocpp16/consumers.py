import json
import asyncio
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from clients.models import Clients
from .models import Ocpp16
from .central_system import ocpp_request, ocpp_conf_from_cp

def channel_logging(cpnumber, channel_name):
  queryset = Clients.objects.filter(cpnumber=cpnumber).values()

  if queryset.count() == 0:
    client = Clients(
      cpnumber = cpnumber,
      channel_name = channel_name,
    )
    client.save()
    print('channel saved successfully')
  else:
    if not (queryset[0]['channel_name'] == channel_name):
      Clients.objects.filter(cpnumber=cpnumber).update(channel_name=channel_name)
      print('channel updated successfully')

class Ocpp16Consumer(WebsocketConsumer):

  def connect(self, subprotocols=['ocpp1.6']):
    try:
      requested_protocols = [item[1] for item in self.scope['headers'] if item[0] == b'sec-websocket-protocol']
    except KeyError:
      print("Client hasn't requested any Subprotocol. Closing Connection")

    if self.scope['subprotocols']:
      print("Protocols Matched: ", self.scope['subprotocols'])
    else:
      print('Protocols Mismatched | Expected Subprotocols: %s, but client supports  %s | Closing connection',
        self.scope['subprotocols'], requested_protocols)
      self.disconnect()

    self.room_group_name = 'all_clients'
    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )
    channel_logging(channel_name=self.channel_name, cpnumber=self.scope['path_remaining'])

    self.accept() 

  def receive(self, text_data):
    # print('self =', dir(self.websocket_connect))
    text_data_json = json.loads(text_data)
    cpnumber = self.scope['path_remaining']

    if text_data_json[0] == 2:
      ocpp_req = {
        "msg_direction" : text_data_json[0],
        "connection_id" : text_data_json[1],
        "msg_name": text_data_json[2],
        "msg_content": text_data_json[3],
        'cpnumber': cpnumber,
      }
      print('OCPP Message : Received from {} : {}'.format(cpnumber, text_data_json))
      Ocpp16.objects.create(
        msg_direction = text_data_json[0],
        connection_id = text_data_json[1],
        msg_name = text_data_json[2],
        msg_content = text_data_json[3],
        cpnumber = cpnumber
      )

      ocpp_conf_json = ocpp_request(ocpp_req)
      if ocpp_conf_json == None:
        pass
      else:
        print('OCPP Conf : Send To {} : {}'.format(cpnumber, ocpp_conf_json))
        Ocpp16.objects.create(
          msg_direction = ocpp_conf_json[0],
          connection_id = ocpp_conf_json[1],
          msg_name = "",
          msg_content = ocpp_conf_json[2],
          cpnumber = cpnumber
        )

        message = ocpp_conf_json

        self.send(text_data=json.dumps(message))

    else:
      ocpp_conf = {
        "msg_direction" : text_data_json[0],
        "connection_id" : text_data_json[1],
        "msg_name": "",
        "msg_content": text_data_json[2],
        'cpnumber': cpnumber,
      }
      print('OCPP Message : Received from {} : {}'.format(cpnumber, text_data_json))
      Ocpp16.objects.create(
        msg_direction = text_data_json[0],
        connection_id = text_data_json[1],
        msg_name = "",
        msg_content = text_data_json[2],
        cpnumber = cpnumber
      )
      ocpp_conf_from_cp(cpnumber, ocpp_conf)

  def ocpp16_message(self, event):
    message = event['message']

    self.send(text_data=json.dumps(message))

  def send(self, text_data=None, bytes_data=None, close=False):
    """
    Sends a reply back down the WebSocket
    """
    if text_data is not None:
        super().send(text_data=text_data)
    elif bytes_data is not None:
        super().send({"type": "websocket.send", "bytes": bytes_data})
    else:
        raise ValueError("You must pass one of bytes_data or text_data")
    if close:
        self.close(close)

  async def get_specific_response(unique_id, timeout):
    print('CardReg response 1: ', response)
    """
    Return response with given unique ID or raise an asyncio.TimeoutError.
    """
    wait_until = time.time() + timeout
    try:
        # Wait for response of the Call message.
        response = await asyncio.wait_for(response_queue.get(), timeout)
    except asyncio.TimeoutError:
        raise
    print('CardReg response 2: ', response)
    if response.unique_id == unique_id:
        print('get specific response for unique ID: %s' % response)
        return response

    print('Ignoring response with unknown unique id: %s', response)
    timeout_left = wait_until - time.time()

    if timeout_left < 0:
        raise asyncio.TimeoutError

    return await get_specific_response(unique_id, timeout_left)


