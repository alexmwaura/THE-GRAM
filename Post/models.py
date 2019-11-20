from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from django.urls import reverse
import datetime


# Create your models here.




class Post(models.Model):
    profile_user = models.ForeignKey(Profile, on_delete=models.CASCADE,)

    title = models.CharField(max_length = 30)
    cover = models.ImageField(upload_to = 'media/images')
    account_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    date_posted = models.DateField(auto_now=True) 
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)



    class Meta:
        ordering = ['-date_posted']
    

    def __str__(self):
        return self.title





    def get_absolute_url(self):
        return reverse('insta-home',kwargs={'date_posted':self.date_posted})


    @classmethod
    def get_user(cls,account_user):
        post = cls.objects.filter(account_user__username__icontains = account_user)
        return post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    text = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)





    class Meta:
        ordering = ['created_date']  







    def __str__(self):
        return 'Comment by {} on '.format(self.user, self.created_date)


    def get_absolute_url(self):
        return reverse('insta-home',)

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.all()
        return comments

    @classmethod
    def get_post_comments(cls,pk):
        post = Post.objects.get(pk=pk)
        comments = []
        all_comments = Comment.objects.filter(post_id = post.id).all()
        comments += all_comments
        return comments    



class Contact(models.Model):
    """docstring for Contact."""
    user_from = models.ForeignKey(User,on_delete=models.CASCADE, related_name='rel_from_set')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return    '{} follows {}'.format(self.user_from, self.user_to)

models.ManyToManyField('self', through=Contact,related_name='followers', symmetrical=False)