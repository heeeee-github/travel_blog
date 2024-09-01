from django import forms
from .models import Post, Category, Image, Video, Audio, Comment, Profile
from django.forms import modelformset_factory
class PostForm(forms.ModelForm) : 
        category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="전체",
        required=False
    )
        class Meta : 
            model = Post 
            fields = ['title', 'content', 'category']
            widgets = {
                'category': forms.Select()  # 기본 선택 위젯을 사용
            }
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
        
ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3, can_delete=True)
VideoFormSet = modelformset_factory(Video, form=VideoForm, extra=3, can_delete=True)
AudioFormSet = modelformset_factory(Audio, form=AudioForm, extra=3, can_delete=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
    
    # 선택적 필드 추가 (예: username은 User 모델의 필드이므로 별도 처리)
    username = forms.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        # instance는 user.profile이 전달되므로, username을 초기값으로 설정
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = user.username

    def save(self, commit=True):
        # Save the user instance
        user = self.instance.user
        user.username = self.cleaned_data.get('username')
        user.save()

        # Save the profile instance
        profile = super().save(commit=commit)
        return profile