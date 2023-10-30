from django.contrib import admin

# Register your models here.
# admin.py
from .models import Bot, Procedimento, Acao

admin.site.register(Bot)
admin.site.register(Procedimento)
admin.site.register(Acao)
