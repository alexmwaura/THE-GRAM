from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from django.urls import reverse
import datetime


# Create your models here.




class Post(models.Model):
    profile_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts',default = timezone.now)

    title = models.CharField(max_length = 30)
    cover = models.ImageField(upload_to = 'media/images')
    account_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    date_posted = models.DateField(auto_now=True) 
    rating_count = models.IntegerField(default=0)



    class Meta:
        ordering = ['-date_posted']
    

    def __str__(self):
        return self.title






    def get_absolute_url(self):
        return reverse('insta-home',kwargs={'date_posted':self.date_posted})





class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts',)  
    text = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)



    class Meta:
        ordering = ['created_date']  


    def approve(self):
        self.approved_comment = True
        self.save()




    def __str__(self):
        return 'Comment by {} on '.format(self.user, self.created_date)


    def get_absolute_url(self):
        return reverse('insta-home',)

class FollowersAndFollowing(models.Model):
    """
    List of followers and following
    """
    
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='followed_by')
    followed_to = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='followed_to')
    created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.followed_by.first_name + '-' + str(self.followed_to.first_name)        