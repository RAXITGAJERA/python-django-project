import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from  embed_video.fields  import  EmbedVideoField
from django.utils.timezone import now


user_country_CHOICES = [
    ('null', 'Null'),
    ('india', 'India'),
    ('austrila', 'Austrila'),
]

user_city_CHOICES = [
    ('null', 'Null'),
    ('rajkot', 'Rajkot'),
    ('junagadh', 'Junagadh'),
]

block_unblock_CHOICES = [
    ('block', 'Block'),
    ('unblock', 'Unblock'),
]

class signup(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=250)
    email = models.EmailField(_('email address'), unique=True)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_fullname = models.CharField(max_length=200, blank=True)
    user_address = models.CharField(max_length=200, blank=True)
    user_gender = models.CharField(max_length=200, blank=True)
    user_country = models.CharField(max_length=200, choices=user_country_CHOICES, default='null')
    user_city = models.CharField(max_length=200, choices=user_city_CHOICES, default='null')
    block_unblock = models.CharField(max_length=10, choices=block_unblock_CHOICES, default='unblock')
    USERNAME_FIELD ='email'


    objects =  CustomUserManager()

class video(models.Model):
    Video_name = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    Video_link = EmbedVideoField()
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)

    def __str__(self):
        return self.Video_name
    
class videocommets(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    post = models.ForeignKey(video, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment