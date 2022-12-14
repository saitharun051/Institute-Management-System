# Generated by Django 4.0.3 on 2022-05-19 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('file', models.ImageField(upload_to='chat/static')),
                ('fid', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('fschool', models.CharField(max_length=100)),
                ('cabin', models.CharField(max_length=100)),
                ('Fdep', models.CharField(max_length=100)),
                ('femail', models.CharField(max_length=100)),
                ('fmob', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reg', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('YOJ', models.CharField(max_length=100)),
                ('PHNO', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to='chat/static')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(blank=True, null=True)),
                ('to_user', models.CharField(max_length=60)),
                ('from_user', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user_has_seen', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chat.chat')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
