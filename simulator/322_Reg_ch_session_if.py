import asyncio
import logging
from chargepoint import ChargePoint

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)

from ocpp.routing import on
from ocpp.v16 import call, call_result
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import RegistrationStatus, Action

logging.basicConfig(level=logging.INFO)

async def heartbeat_send(cp):
    while True:
        await cp.send_heartbeat()
        await asyncio.sleep(cp.heartbeat_interval)

async def main():

    async with websockets.connect(
        'ws://127.0.0.1:8000/webServices/ocpp/202021',
        subprotocols=['ocpp1.6']
    ) as ws:

        cp = ChargePoint('202021', ws)

        await asyncio.gather(
          cp.start(), 
          cp.send_boot_notification(),
          cp.send_status_notification('Available'),
          heartbeat_send(cp),
        #   cp.send_stop_transaction(),
        #   cp.send_status_notification('Finishing'),
        #   cp.send_status_notification('Available'),
          cp.send_authorize('0000000000150049'),
          cp.send_status_notification('Preparing'),
          cp.send_start_transaction('0000000000150049'),
          cp.send_status_notification('Charging'),
        #   cp.send_meter_value(),
          cp.send_stop_transaction(),
          cp.send_status_notification('Finishing'),
          cp.send_status_notification('Available'),
        #   heartbeat_send(cp, heartbeat_interval)
        )

if __name__ == '__main__':
    try:
        # asyncio.run() is used when running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
