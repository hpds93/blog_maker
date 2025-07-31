"""Defines URL patterns for myapp."""
from django.urls import path, include
from . import views


app_name = 'myapp'
urlpatterns = [
    # Home page
    path('index', views.index, name='index'),
    path('my_blogs', views.my_blogs, name='my_blogs'),
    path('new_blog', views.new_blog, name='new_blog'),
    path('edit_blog_<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('posts_<int:blog_id>', views.posts, name='posts'),
    path('new_post_<int:blog_id>', views.new_post, name='new_post'),
    path('edit_post_<int:post_id>', views.edit_post, name='edit_post'),

    path('account/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register')
]