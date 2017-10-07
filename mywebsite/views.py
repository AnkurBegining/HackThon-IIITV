from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
def firstPage(request):
    return render(request, 'mywebsite/firstPage.html', {})

def workshop(request):
    return render(request, 'mywebsite/workshop.html')

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'mywebsite/firstPage.html', args)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mywebsite/post_list.html', {'posts': posts})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mywebsite/post_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mywebsite:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mywebsite/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mywebsite/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('mywebsite:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'mywebsite/add_comment_to_post.html', {'form': form})

@login_required()
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('mywebsite:post_detail', pk=comment.post.pk)


@login_required()
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)