from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def home(request):
    n=Notification.objects.filter(Q(user_has_seen=False) & Q(to_user=str(request.user.username))).count()
    return render(request, 'chat/Home.html',{'count':n})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'chat/Login/login.html')

def info(request):
    students = Student.objects.all()
    return render(request, 'Personal.html', {'students':students})

def logout(request):
    auth.logout(request)
    return redirect('/')


def Queries(request):
    faculty=Faculty.objects.filter(Q(fid=str(request.user.username)))
    print(faculty)
    if not faculty:
        faculty = Faculty.objects.all()
        noti=[]
        for i in faculty:
            noti.append(Notification.objects.filter(Q(user_has_seen=False) & Q(from_user=i.fid)).count())
        s1=zip(faculty,noti)
        print(faculty)
        print(noti)
        return render(request, 'Queries.html',{'n':s1})
    else:
        faculty = ChatRoom.objects.filter(Q(name__icontains=str(request.user.username)))
        f=[]
        for i in faculty:
            f.append(i.name)
        r=[]
        for i in f:
            r.append(i[0:i.index('v')])
        students=Student.objects.filter(Q(reg__in=r))
        noti=[]
        for i in students:
            noti.append(Notification.objects.filter(Q(user_has_seen=False) & Q(from_user=i.reg)).count())
        print(students)
        s1=zip(students,noti)
        return render(request, 'Queries1.html',{'faculty':faculty,'n':s1})

class Index(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'index.html')
		
class Room(LoginRequiredMixin, View):
    def get(self, request, room_name):
        room = ChatRoom.objects.filter(name=str(room_name)).first()
        chats = []
        if room:
            chats = Chat.objects.filter(room=room)
            n1=Notification.objects.filter(Q(chat__in=chats))
            n2=n1.filter(Q(to_user=request.user.username))
            print(n2)
            for c in n2:
                c.user_has_seen=True
                c.save()
        else:
            room = ChatRoom(name=str(room_name))
            room.save()
        return render(request, 'room.html', {'room_name': room_name, 'chats': chats})