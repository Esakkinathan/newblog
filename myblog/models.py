from django.db import models
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100,blank=True,null=True)
    web_url = models.CharField(max_length=255,null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    github_url = models.CharField(max_length=255,null=True,blank=True)
    linkedin_url = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse("article_detail", args=str(self.id))
        return reverse("home")

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255,default='uncategorized')
    likes = models.ManyToManyField(User,related_name="blog_posts",blank=True,null=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse("article_detail", args=str(self.id))
        return reverse("home")

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse("article_detail", args=str(self.id))
        return reverse("home")

