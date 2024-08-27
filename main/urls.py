from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('enter_blog/', views.enter_blog, name = 'enter_blog')
]