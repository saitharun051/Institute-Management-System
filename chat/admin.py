from django.contrib import admin
from .models import Chat, ChatRoom, Student,Faculty,Notification
# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(Chat)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Notification)