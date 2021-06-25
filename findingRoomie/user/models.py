from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Userinfo(models.Model):
    realname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    studentID = models.IntegerField()

    thisisme = models.CharField(max_length=200)
    profilePic = ImageField()

    sleepT  = models.DateTimeField()
    clean = models.CharField(max_length=100)
    cook = models.BooleanField()
    smoke = models.BooleanField()
    sleepHabit = models.CharField(max_length=100)
    values = models.CharField(max_length=50)

    budget = models.IntegerField()
    area = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.nickname