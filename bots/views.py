from rest_framework import generics
from .models import Bot
from .serializers import BotSerializer

class BotListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

class BotDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer