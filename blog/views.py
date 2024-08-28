from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Post, Category
from .forms import PostForm  # forms.py에서 작성한 폼을 사용

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()  # 모든 카테고리 가져오기
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  
        raise PermissionDenied  
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_update.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  # 작성자와 현재 사용자가 다르면
        raise PermissionDenied  # 권한이 없다는 예외를 발생시킴
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    
    return render(request, 'blog/post_delete.html', {'post': post})

def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')

    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})
