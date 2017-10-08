from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    titleImage = models.FileField(null=True, blank=True)
    text = models.TextField()
    ideaCategories = models.TextField()
    cofounderOfIdeas = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('mywebsite.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class CreateWorkshop(models.Model):
    WorkshopName = models.CharField(max_length=50, default="")
    StartDate = models.DateField()
    EndDate = models.DateField()
    Subject = models.CharField(max_length=50)
    Topic = models.CharField(max_length=50)
    Venue = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.WorkshopName

class CreateBlog(models.Model):
    BlogName = models.CharField(max_length=50)
    BlogAddressFirstName = models.CharField(max_length=100)
    BlogDescription = models.CharField(max_length=10000)
    Comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.BlogName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
