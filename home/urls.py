from django.urls import path
from .views import BotListView, BotCreateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bots/', BotListView.as_view(), name='bots:list'),
    path('bots/create/', BotCreateView.as_view(), name='bots:create'),
]
