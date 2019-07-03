from rest_framework.generics import ListAPIView, RetrieveAPIView

from chat.models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageListView(ListAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class ChatMessageDetailView(RetrieveAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer