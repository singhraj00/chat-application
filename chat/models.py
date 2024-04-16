from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    profile_picture = models.ImageField(upload_to='profile_img')

class ThreadManager(models.Manager):
    def by_user(self,**kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs     


class Thread(models.Model):
    first_person = models.ForeignKey(User,on_delete=models.CASCADE,related_name='thread_first_person',null=True,blank=True)
    second_person = models.ForeignKey(User,on_delete=models.CASCADE,related_name='thread_second_person',null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = ThreadManager()

    class Meta:
        unique_together = ['first_person','second_person']




class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE,null=True,blank=True,related_name='chatmessage_thread')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)