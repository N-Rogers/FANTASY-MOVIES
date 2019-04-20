from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} profile'

def create_profile(sender, **kwags):
    if kwags['created']:
        userprofile = profile.objects.create(user=kwags['instance'])
        
post_save.connect(create_profile, sender=User)
