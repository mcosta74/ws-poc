import asyncio
import datetime
import logging
import os

import websockets


async def consumer_handler(websocket: websockets.WebSocketServerProtocol, path: str):
    logging.info('Handler for: %s, %s', websocket.host, path)

    async for message in websocket:
        logging.info('>: %s', message)

        await websocket.send(f'{datetime.datetime.utcnow().isoformat()} {message}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    logging.info('Starting server...')

    ws_host = os.environ.get('WS_HOST', '0.0.0.0')
    ws_port = int(os.environ.get('WS_PORT', 6875))

    server = websockets.serve(consumer_handler, ws_host, ws_port)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
