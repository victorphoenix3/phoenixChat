# Serializers allow complex data such as querysets 
# and model instances to be converted 
# to native Python datatypes that can 
# then be easily rendered into JSON, XML or other content types.

from rest_framework import serializers

from chat.models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'