from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User                             # this is database creation with the system
from django.urls import reverse
from ckeditor.fields import RichTextField                                       #add feathers for textbody

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):                                                          #display with title + author
        return self.name

    def get_absolute_url (self):
        return reverse ('home') 

class Prof_inf(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500)
    profie_pic=models.ImageField(null=True,blank=True,upload_to='images/profile')
    web_site=models.CharField(max_length=200,null=True,blank=True)
    facebook_url=models.CharField(max_length=200,null=True,blank=True)
    twitter_utl=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return str((self.user))


class post(models.Model):
    title=models.CharField(max_length=200)
    header_image=models.ImageField(null=True,blank=True,upload_to='images/')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(null=True,blank=True)                                    #add feathers for textbody go for add_post.html and add {{form.media}}
    snippet=models.CharField(max_length=250 ,null=True,blank=True,default='')                   
    post_data=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=250,default='')
    likes=models.ManyToManyField(User,related_name="blog_posts")
    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):                                                    #display with title + author
        return self.title +' | ' + str(self.author)


    def get_absolute_url (self):
        return reverse ('article_detail',args=(str(self.id)))            #return to article page with id post creation now
        #return reverse ('article_detail',args=(str(self.id)))          #return to home page