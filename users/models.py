from django.db import models
from django.contrib.auth.models import User
from PIL import Image
 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'download.png', upload_to ='profile_pics/')

    def __str__(self):
        return f'{self.user.username} Profile'




class UserFollowing(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)    
   