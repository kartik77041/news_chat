from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, chat
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket Connected...', event)
        print("channels layer",self.channel_layer)
        print("channels name",self.channel_name)
        group_name = self.scope['url_route']['kwargs']['groupkaname']
        async_to_sync(self.channel_layer.group_add)(group_name,self.channel_name)
        self.send({
            'type':'websocket.accept'
            })
    
    def websocket_receive(self, event):
        group_name = self.scope['url_route']['kwargs']['groupkaname']
        data = json.loads(event['text'])
        groups = Group.objects.filter(name=group_name).first()
        if self.scope['user'].is_authenticated:
            chats = chat(content = data['msg'], group = groups )
            chats.save()
            data['user'] = self.scope['user'].username
            async_to_sync(self.channel_layer.group_send)(
                group_name,
                {
                    'type':'chat.message',
                    'message' : json.dumps(data)
                }
            )
        else:
           self.send(
           {
           'type':'websocket.send',
           'text':json.dumps({"msg":"Login Required"})
           })

    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message']
            })
    
    def websocket_disconnect(self, event):
        print('websocket Disconnected...', event)
        print("channels layer",self.channel_layer)
        print("channels name",self.channel_name)
        group_name = self.scope['url_route']['kwargs']['groupkaname']
        async_to_sync(self.channel_layer.group_discard)(group_name,self.channel_name)
        self.send({
            'type':'websocket.accept'
            })
        raise StopConsumer()