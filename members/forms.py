from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User 
from django import forms
from theblog.models import Prof_inf



class Sign_Up(UserCreationForm):
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

        widgets = {

        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'password1':forms.TextInput(attrs={'class':'form-control'}),
        'password2':forms.TextInput(attrs={'class':'form-control'}),
    }
    

class profile(UserChangeForm):
    #is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password',"is_staff","is_active","date_joined","last_login")


        widgets = {

        'username'   :forms.TextInput(attrs={'class':'form-control'}),
        'first_name' :forms.TextInput(attrs={'class':'form-control'}),
        'last_name'  :forms.TextInput(attrs={'class':'form-control'}),
        'email'      :forms.TextInput(attrs={'class':'form-control'}),
        'is_staff'   :forms.CheckboxInput(attrs={'class':'form-check'}),
        "is_active"  :forms.CheckboxInput(attrs={'class':'form-check'}),
        "date_joined":forms.TextInput(attrs={'class':'form-control'}),
        "last_login" :forms.TextInput(attrs={'class':'form-control'}),

    }   


class create_form(forms.ModelForm):
    class Meta:
        model=Prof_inf
        fields=('bio','profie_pic','web_site','facebook_url','twitter_utl')


        widgets = {

        'bio' :forms.Textarea(attrs={'class':'form-control'}),
        'web_site'     :forms.TextInput(attrs={'class':'form-control'}),
        'facebook_url' :forms.TextInput(attrs={'class':'form-control'}),
        'twitter_utl' :forms.TextInput(attrs={'class':'form-control'}),
        
    } 