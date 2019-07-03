import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread, ChatMessage

#Async allows connection and reconnection without reloading the page
class ChatConsumer(AsyncConsumer):
    
    # to handle if a client socket is connecting to the server.
    async def websocket_connect(self,event):
        print ("connected", event)
        
        user1 = self.scope['user']
        user2 = self.scope['url_route']['kwargs']['username']
        # print(user1,user2)
        thread_obj = await self.get_thread(user1, user2)
        self.thread_obj=thread_obj
        # print(thread_obj.id)
        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    # to handle when the server receive messages from client socket
    async def websocket_receive(self,event):
        #this maps to type: websocket.recieve
        print ("recieved", event)
        text = event.get('text', None)
        if text is not None:
            msg = json.loads(text).get('message')
            user = self.scope['user']
            username = 'default'
            print (msg)
            if user.is_authenticated:
                username = user.username
            response = {
                'message': msg,
                'username': username
            }
            await self.create_chat_message(user,msg)
            # event = {
            #     "type": "websocket.send",
            #     "text": json.dumps(response)
            # }
            await self.channel_layer.group_send(
                self.chat_room,{
                    "type": "chat_message",
                    "text": json.dumps(response)
                    }
            )
            
    async def chat_message(self, event):
        print ('message', event)
        await self.send({
            "type": "websocket.send",
            "text": event["text"]            
        })


    # to handle if a client socket is disconnecting to the server
    async def websocket_disconnect(self,event):
        print ("disconnected", event)

    @database_sync_to_async #to avoid memory leaks and too many request
    def get_thread(self, user, other_username):
        return Thread.objects.get_or_new(user, other_username)[0]
    
    @database_sync_to_async #to avoid memory leaks and too many request
    def create_chat_message(self, user, message):
        thread_obj=self.thread_obj
        return ChatMessage.objects.create(thread=thread_obj,user=user,message=message)
    