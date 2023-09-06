from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class post(models.Model):
    image=models.ImageField(upload_to = 'images' , null=True)
    title=models.CharField(max_length=100, null=True)
    author=models.CharField(max_length=100, null=True)
    desc=models.TextField(max_length=200, null=True)
    var=models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    create_date=models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_posts')
    
       
    def __str__(self):
        return self.title
    

class Profile(models.Model):
    profile_picture=models.ImageField(upload_to='profile_picture', null=True)
    bio=models.TextField(max_length=150, null=True)
    car=models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.bio
    
         
class Comment(models.Model):
    related = models.ForeignKey(post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    author_dp=models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.related}"
    
    
class Like(models.Model):
    malik = models.ForeignKey(User, on_delete=models.CASCADE)
    malik_post = models.ForeignKey(post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    
    
    
    
    
    

    

    
