from rest_framework import viewsets, routers
from .models import Chat
from .serializer import ChatSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.order_by('-date')[:50]
    serializer_class = ChatSerializer


router = routers.DefaultRouter()
router.register(r'chats', ChatViewSet)
