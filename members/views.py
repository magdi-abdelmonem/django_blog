from pyexpat import model
from re import template
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm         #it is a built form
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404
from theblog.models import Prof_inf
from .forms import  Sign_Up, profile,create_form
from django import forms

class Edit_proff(generic.UpdateView):
    model= Prof_inf
    template_name="registration/edit_profile.html"
    success_url= reverse_lazy('home') 


class Create_profile(CreateView):
    model=Prof_inf
    form_class=create_form
    template_name="registration/creation_page.html"
    success_url= reverse_lazy('home') 
    
 


class UserRegisterView(generic.CreateView):                
    
    form_class = Sign_Up                                 # i use usercreationform
    template_name="registration/register.html"
    success_url= reverse_lazy('login') 


class Profile(generic.UpdateView):                
    form_class = profile                                 # i use usercreationform
    template_name="registration/profile.html"
    success_url= reverse_lazy('home') 

    def get_object(self):                                   #return with fill auto data
        return self.request.user

    

class User_profile(DetailView):
    model=Prof_inf
    template_name="registration/user_profile.html"

    def get_context_data (self,*args,**kwargs):          #this function for profile user
        users=Prof_inf.objects.all()
        context=super(User_profile,self).get_context_data(*args,**kwargs)
        page_user= get_object_or_404(Prof_inf,id=self.kwargs['pk'])
        context['page_user']=page_user
        return context




