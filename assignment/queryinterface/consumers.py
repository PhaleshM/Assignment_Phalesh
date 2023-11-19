import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_logs(self, event):
        logs = event['logs']
        await self.send(text_data=json.dumps({
            'logs': logs
        }))
