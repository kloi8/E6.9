from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=256, unique=True)


class User(models.Model):
    name = models.CharField(max_length=256, unique=True)
    avatar = models.ImageField(default='default.png', upload_to='media', null=True, blank=True)
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD = 'username'
    def user_list(self):
        users = User.objects.filter().order_by('name')
        return list(users)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
