from django.db import models
from django.contrib.auth.models import User,AbstractUser
# from django.db.models import DateField

# Create your models here.

class MyUser(AbstractUser):
    phone=models.CharField(max_length=20)
    profile_pic=models.ImageField(null=True,upload_to='profilepics',blank=True)
    Bio=models.CharField(null=True,blank=True,max_length=300)

class Posts(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    location=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='images')
    post_date=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(MyUser,related_name='likes')
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.user

class Comments(models.Model): 
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    post_date=models.DateField(auto_now_add=True)


class Storys(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    story=models.ImageField(upload_to='stories')
    create_date=models.DurationField(auto_created=True)

    