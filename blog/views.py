from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Prefetch
from .models import Post, Category, Image, Video, Audio, Comment, Profile, BannedWord
from .forms import PostForm, ImageFormSet, VideoFormSet, AudioFormSet, CommentForm, ProfileForm
from datetime import timedelta
import re

def censor_text(text):
    banned_words = BannedWord.objects.values_list('word', flat=True)
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub("*" * len(word), text)
    return text

def blog_main(request):
    posts = Post.objects.all().order_by('-created_at').prefetch_related('images')
    top_posts = Post.objects.order_by('-views')[:10].prefetch_related('images')
    recent_posts = Post.objects.order_by('-created_at')[:5].prefetch_related('images')

    return render(request, 'blog/blog_main.html', {
        'posts': posts,
        'recent_posts': recent_posts,
        'top_posts': top_posts,
    })
    

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')    
    # 사이드바를 위한 추가 정보
    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-created_at')[:5].prefetch_related('images')

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
        'category': None
    })
    

def popular_post(request):
    # Post 객체를 조회하고 정렬 및 슬라이스
    top_posts = Post.objects.all().order_by('-views')[:5]
    return render(request, 'blog/blog_view.html', {'top_posts': top_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post.objects.prefetch_related('images'), pk=pk)
    comments = post.comments.all()

    session_key = f'viewed_post_{post.pk}'
    if not request.session.get(session_key):
        post.views += 1
        post.save()
        request.session[session_key] = True
        request.session.set_expiry(timedelta(hours=1))  # 1시간 후 쿠키 만료```
        
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    # 사이드바를 위한 추가 정보
    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-created_at')[:5]
    
    return render(request, 'blog/post_detail.html', {
        'post': post, 
        'comments': comments,
        'comment_form': comment_form,
        'categories': categories,
        'recent_posts': recent_posts,
    })

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        video_formset = VideoFormSet(request.POST, request.FILES, queryset=Video.objects.none())
        audio_formset = AudioFormSet(request.POST, request.FILES, queryset=Audio.objects.none())

        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid() and audio_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 글에 검열 기능 적용
            post.content = censor_text(post.content)
            post.save()
        
            for form in image_formset:
                if form.cleaned_data and form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.post = post
                    image.save()

            for form in video_formset:
                if form.cleaned_data and form.cleaned_data.get('video'):
                    video = form.save(commit=False)
                    video.post = post
                    video.save()

            for form in audio_formset:
                if form.cleaned_data and form.cleaned_data.get('audio'):
                    audio = form.save(commit=False)
                    audio.post = post
                    audio.save()
                    
            return redirect('post_list')
                    
    else:
        form = PostForm()
        image_formset = ImageFormSet(queryset=Image.objects.none())
        video_formset = VideoFormSet(queryset=Video.objects.none())
        audio_formset = AudioFormSet(queryset=Audio.objects.none())

    return render(request, 'blog/post_create.html', {
        'form': form,
        'image_formset': image_formset,
        'video_formset': video_formset,
        'audio_formset': audio_formset,
    })

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  
        raise PermissionDenied
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.filter(post=post))
        video_formset = VideoFormSet(request.POST, request.FILES, queryset=Video.objects.filter(post=post))
        audio_formset = AudioFormSet(request.POST, request.FILES, queryset=Audio.objects.filter(post=post))
        
        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid() and audio_formset.is_valid():
            # 글에 검열 기능 적용
            post.content = censor_text(post.content)
            post = form.save()
            
            for image_form in image_formset:
                if image_form.cleaned_data and image_form.cleaned_data.get('image'):
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()

            for video_form in video_formset:
                if video_form.cleaned_data and video_form.cleaned_data.get('video'):
                    video = video_form.save(commit=False)
                    video.post = post
                    video.save()

            for audio_form in audio_formset:
                if audio_form.cleaned_data and audio_form.cleaned_data.get('audio'):
                    audio = audio_form.save(commit=False)
                    audio.post = post
                    audio.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        image_formset = ImageFormSet(queryset=Image.objects.filter(post=post))
        video_formset = VideoFormSet(queryset=Video.objects.filter(post=post))
        audio_formset = AudioFormSet(queryset=Audio.objects.filter(post=post))
    
    return render(request, 'blog/post_update.html', {
        'form': form,
        'image_formset': image_formset,
        'video_formset': video_formset,
        'audio_formset': audio_formset,
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  # 작성자와 현재 사용자가 다르면
        raise PermissionDenied  # 권한이 없다는 예외를 발생시킴
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    
    return render(request, 'blog/post_delete.html', {'post': post})

def posts_by_category(request, pk):
    # 사이드바를 위한 추가 정보
    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-created_at')[:5]
    
        # 특정 카테고리 게시글 보기
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')

    return render(request, 'blog/posts_by_category.html', {
        'category': category,
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
    })
    
@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            print(comment.post.pk)  
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_edit.html', {'form': form, 'comment' : comment})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        raise PermissionDenied

    if request.method == "POST":
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)

    return render(request, 'blog/comment_delete.html', {'comment': comment})

@login_required
def comment_reply(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = get_object_or_404(Post, pk=request.POST['post'])
            reply_to_pk = request.POST.get('reply_to')
            if reply_to_pk:
                reply_to_comment = get_object_or_404(Comment, pk=reply_to_pk)
                comment.parent = reply_to_comment
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    return redirect('index')

@login_required
def mypage_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(author=user)

    return render(request, 'blog/mypage.html', {'user': user, 'profile': profile, 'posts': posts})

@login_required
def edit_profile(request):
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile, user=user)
        if form.is_valid():
            form.save()
            return redirect('mypage', username=user.username)
    else:
        form = ProfileForm(instance=user.profile, user=user)
    
    context = {
        'form': form
    }
    return render(request, 'blog/edit_profile.html', context)
