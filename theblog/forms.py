from random import choices
from django import forms
from .models import Category, post ,Prof_inf


#choices=[('islamic','islamic'),('coding','coding'),('funny','funny')]                   #limit chices

choices=Category.objects.all().values_list('name','name')                                  #take data category from category direct



class PostForm(forms.ModelForm):                                                        #class form for post page and style it that i want
    class Meta:
        model=post
        fields=('title','author','category','body','snippet','header_image')

        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id': 'elder','type':'hidden'}),
            'category':forms.Select(choices=choices ,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control','placeholder':'Post the article snippet here'}),
        }



class UpdateForm(forms.ModelForm):                    #class form for update page and style it that i want
    class Meta:
        model=post
        fields=('title','author','category','body','snippet','header_image')

        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choices ,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control','placeholder':'Post the article snippet here'}),
            
        }


class CategoryForm(forms.ModelForm):                    #class form for category page and style it that i want
    class Meta:
        model=Category
        fields='__all__'


