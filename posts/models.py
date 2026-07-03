
from django.db import models
from django.contrib.auth.models import User 
"""class Author(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
"""

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title



