from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
# Create your views here.

def http_recp(request):
    return HttpResponse('Hello 4 month')


def html_hello(request):
    return render(request, 'hello.html')


def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        form = CommentForm()
        return render(request, 'posts/post_detail.html', {'post': post, 'form': form})


def create_post_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/create_post.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/create_post.html', {'form': form})
        form.save()
        return redirect('/post/posts/')


def comment_create_view(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(request,
                          'posts/post_detail.html',
                          context={'form': form})
        review = form.save(commit=False)
        review.post_id = post_id
        review.save()
        return redirect(f'/post/posts/{post_id}')