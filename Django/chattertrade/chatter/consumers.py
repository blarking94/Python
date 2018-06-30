from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from random import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'currencies_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        print("the received")
        print(text_data_json)

        message = text_data_json['message']
        username = text_data_json['username']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        print("receive message from group")
        print(event)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username' : username,
            'message': message
        }))
