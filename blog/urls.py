from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    
    path('accounts/', include('accounts.urls')),
    
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/reply/', views.comment_reply, name='comment_reply'),

    path('mypage/<str:username>/', views.mypage_view, name='mypage'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
