from django.urls import path
from .views import ChatMessageListView, ChatMessageDetailView

urlpatterns = [
    path('chatMessage/',ChatMessageListView.as_view()),
    path('chatMessage/<pk>/',ChatMessageDetailView.as_view())
]