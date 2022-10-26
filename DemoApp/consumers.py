from channels.generic.websocket import WebsocketConsumer
import logging

class DemoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, **kwargs):
        logger = logging.getLogger('django')
        logger.info(text_data)
        self.send(text_data=text_data)
