import asyncio
import logging
import os

import websockets


async def producer():
    ws_host = os.environ.get('WS_HOST', 'localhost')
    ws_port = int(os.environ.get('WS_PORT', 6875))

    uri = f'ws://{ws_host}:{ws_port}/client'

    logging.info('Connecting to <%s>...', uri)
    async with websockets.connect(uri) as websocket:
        logging.info('Connected')

        while True:
            await websocket.send('Hello')

            reply = await websocket.recv()
            logging.info('> %s', reply)

            await asyncio.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    asyncio.run(producer())
