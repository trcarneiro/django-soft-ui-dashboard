from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Bot
from .forms import BotForm


# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

class BotListView(View):
    def get(self, request):
        bots = Bot.objects.all()
        return render(request, 'bots/list.html', {'bots': bots})

class BotCreateView(View):
    def get(self, request):
        form = BotForm()
        return render(request, 'bots/create.html', {'form': form})

    def post(self, request):
        form = BotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bots:list')
        return render(request, 'bots/create.html', {'form': form})