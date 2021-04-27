from django.db import models

# Create your models here.

class message(models.Model):
    textmess = models.CharField(max_length=400)
    usersend = models.CharField(max_length=20)
    userto = models.CharField(max_length=20)
    year = models.IntegerField()
    mon = models.IntegerField()
    day = models.IntegerField()
    Hour = models.IntegerField()
    mins = models.IntegerField()
    sec = models.IntegerField()
class friend(models.Model):
    requset_frinend = models.CharField(max_length=20)
    request_to = models.CharField(max_length=20)
    accepted_friend = models.CharField(max_length=20)
    accepted_to = models.CharField(max_length=20)
    nos_friends = models.CharField(max_length=20)
class img(models.Model):
    image = models.ImageField(upload_to='pics')
    userr = models.CharField(max_length=20)
class bio(models.Model):
        bio = models.CharField(max_length=80)
        userr2 = models.CharField(max_length=20)