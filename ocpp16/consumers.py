import json
from channels.generic.websocket import WebsocketConsumer

from .central_system import ocpp_request
from msglog.models import Msglog
from .models import Ocpp16
# from asgiref.sync import async_to_sync

def msglogging(msg):
  msglog = Msglog(
    cpname = msg['cpname'],
    connection_id = msg['connection_id'],
    msg_direction = msg['msg_direction'],
    msg_name=msg['msg_name'],
    msg_content=msg['msg_content']
  )
  msglog.save()

def consumerlogging(cpname, consumer):
  queryset = Ocpp16.objects.filter(cpname=cpname).values()

  if queryset.count() == 0:
    ocpp16 = Ocpp16(
      cpname = cpname,
      consumer = consumer,
    )
    ocpp16.save()
    print('consumer saved successfully')
  else:
    if not (queryset[0]['consumer'] == consumer):
      Ocpp16.objects.filter(cpname=cpname).update(consumer=consumer)
      print('consumer updated successfully')

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

    self.accept()
    consumerlogging(self.scope['path_remaining'], self.scope['client'])
    print('self = ', dir(self))

  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    ocpp_req = {
      "msg_direction" : text_data_json[0],
      "connection_id" : text_data_json[1],
      "msg_name": text_data_json[2],
      "msg_content": text_data_json[3],
      'cpname': self.scope['path_remaining'],
    }
    print('OCPP Message : Received from {} : {}'.format(ocpp_req['cpname'], text_data_json))
    msglogging(ocpp_req)

    ocpp_conf = ocpp_request(ocpp_req)

    print('OCPP Conf : Send To {} : {}'.format(ocpp_req['cpname'], ocpp_conf))
    ocpp_conf_json = {
      "msg_direction" : ocpp_conf[0],
      "connection_id" : ocpp_conf[1],
      "msg_name": "",
      "msg_content": ocpp_conf[2],
      'cpname': self.scope['path_remaining'],
    }
    msglogging(ocpp_conf_json)
    self.send(text_data=json.dumps(ocpp_conf))

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
