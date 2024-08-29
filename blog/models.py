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
class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.post.title}"
class Video(models.Model):
    post = models.ForeignKey(Post, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Video for {self.post.title}"
class Audio(models.Model):
    post = models.ForeignKey(Post, related_name='audios', on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audios/')

    def __str__(self):
        return f"Audio for {self.post.title}"
    
class Comment(models.Model) : 
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
    def __str__(self) : 
        return f"댓글 : {self.author} on {self.post}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}의 프로필"    