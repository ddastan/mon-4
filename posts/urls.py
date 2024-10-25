from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello_html/', views.html_hello),
    path('hello_http/', views.http_recp),
    path('posts/', views.post_list_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('create_post/', views.create_post_view),
    path('posts/<int:post_id>/create_comment/', views.comment_create_view),
]