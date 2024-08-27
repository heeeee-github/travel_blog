from django.contrib.auth.models import User 
from django.db import models

class Category(models.Model) : 
    name = models.CharField(max_length = 100 , unique = True)
    def __str__(self) : 
        return self.name

class Post(models.Model) : 
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name = 'posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

    def __str__(self) : 
        return self.title