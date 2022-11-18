from django.db import models
from django.contrib.auth.models import User
from django.db import connections

class Chat(models.Model):
	content = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)

class ChatRoom(models.Model):
	name = models.CharField(max_length=255)

class Student(models.Model):
    id=models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    reg = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    YOJ = models.CharField(max_length=100)
    PHNO = models.CharField(max_length=100)
    file = models.ImageField(upload_to="chat/static")

class Faculty(models.Model):
    id=models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    file = models.ImageField(upload_to="chat/static")
    fid = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    fschool = models.CharField(max_length=100)
    cabin = models.CharField(max_length=100)
    Fdep = models.CharField(max_length=100)
    femail = models.CharField(max_length=100)
    fmob = models.CharField(max_length=100)

class Notification(models.Model):
    # 
    notification_type = models.IntegerField(null=True, blank=True)
    to_user = models.CharField(max_length=60)
    from_user = models.CharField(max_length=60)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    user_has_seen = models.BooleanField(default=False)
# Create your models here.
