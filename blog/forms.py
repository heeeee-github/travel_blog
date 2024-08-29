from django import forms
from .models import Post, Image, Video, Audio, Comment, Profile
from django.forms import modelformset_factory
class PostForm(forms.ModelForm) : 
    class Meta : 
        model = Post 
        fields = ['title', 'content', 'category']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video']
class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['audio']
        
ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5, can_delete=True)
VideoFormSet = modelformset_factory(Video, form=VideoForm, extra=5, can_delete=True)
AudioFormSet = modelformset_factory(Audio, form=AudioForm, extra=5, can_delete=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'location']