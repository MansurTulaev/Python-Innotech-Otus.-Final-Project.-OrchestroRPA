from django.urls import path
from .views import BotListCreateAPIView, BotDetailAPIView

urlpatterns = [
    path('', BotListCreateAPIView.as_view(), name='bot-list-create'),
    path('<int:pk>/', BotDetailAPIView.as_view(), name='bot-detail'),
]