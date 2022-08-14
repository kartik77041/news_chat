from django.contrib import admin
from .models import chat, Group
@admin.register(chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'content', 'timestamp', 'group']

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'name']