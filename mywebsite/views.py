from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm, CreateWorkshopForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from mywebsite.forms import SignUpForm
from mywebsite.tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import login
import smtplib

# Create your views here.
def firstPage(request):
    return render(request, 'mywebsite/firstPage.html', {})

def workshop(request):
    return render(request, 'mywebsite/workshop.html')

def createworkshop(request):
    return render(request, 'mywebsite/createWorkshop.html')

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

def CreateWorkshop(request):
    if request.method == "POST":
        form = CreateWorkshopForm(request.POST)
        if form.is_valid():
            createworkshoppost = form.save(commit=False)
            createworkshoppost.WorkshopName = request.user
            createworkshoppost.save()
            return  redirect('/workshop/')
    else:
        form = CreateWorkshopForm()
        return render(request,'mywebsite/createWorkshop.html',{'form':form})



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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your InterAdicr Account'
            message = render_to_string('mywebsite/account_activation_email.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': account_activation_token.make_token(user), })
            user.email_user(subject, message)
            send_verification_mail(user.email, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'mywebsite/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'mywebsite/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        user.is_active = True
        return render(request, 'mywebsite/firstPage.html', {})
    else:
        return render(request, 'mywebsite/profile.html', {})


email_address = 'deployment334@gmail.com'
email_password = 'Dipadi@god5'


def send_verification_mail(email, msg):
    print("send verificaion mail")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, email, msg)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")