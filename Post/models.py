from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.




class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now) 


    def __str__(self):
        return  self.title      