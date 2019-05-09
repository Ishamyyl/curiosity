import asyncio
from json import dumps, loads
from pathlib import Path
from subprocess import Popen

from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol


class App(WebSocketServerProtocol):
    def onConnect(self, request):
        print(f"Client connecting: {request.peer}")

    def onOpen(self):
        print("WebSocket connection open.")

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket connection closed: {reason}")

    def onMessage(self, payload, *args, **kwargs):
        payload = loads(payload)
        print(f"Text message received: {payload}")
        action = payload.pop("action", "default_action")
        getattr(self, action)(payload, *args, **kwargs)

    def sendMessage(self, payload, *args, **kwargs):
        return super().sendMessage(bytes(dumps(payload), "utf-8"), *args, **kwargs)

    def default_action(self, payload):
        print(payload)

    def echo(self, payload, *args, **kwargs):
        self.sendMessage(payload, *args, **kwargs)


class Server(WebSocketServerProtocol):
    def __init__(self, protocol=App, hostname="127.0.0.1", port=9000, address="0.0.0.0"):
        factory = WebSocketServerFactory(f"ws://{hostname}:{port}")
        factory.protocol = protocol

        loop = asyncio.get_event_loop()
        coro = loop.create_server(factory, address, port)
        server = loop.run_until_complete(coro)

        try:
            path = Path("curiosity/index.html").resolve()
            Popen(["bin/cefclient/cefclient.exe", f"--url=file://{path}", "--allow-file-access-from-files"])
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.close()
            loop.close()
