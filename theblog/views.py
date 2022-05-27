from multiprocessing import context
from urllib import request
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy ,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView   #libraries 
from .models import Category, post
from .forms import CategoryForm, PostForm,UpdateForm
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    
    post=get_object_or_404(post,id= request.POST.get('post_id'))
    post.likes.add(request.user)
    
    return HttpResponseRedirect (reverse('article_detail',args=[str(pk)]))
 

class HomeView(ListView):                              #create class for home page
    model = post
    template_name='home.html'
    #ordering =['-id']                                  #order by id
    ordering =['-post_data']                            #order by data


    def get_context_data (self,*args,**kwargs):          #this function for a category data name to category navbar
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context

class ArticleDetailView(DetailView):                   #create class for articles page
    model = post
    template_name = 'article_details.html'


    def get_context_data(self,*args,**kwargs):          #this function for a category data name to category navbar
        cat_menu=Category.objects.all()
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff=get_object_or_404(post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        return context




class AddPostView(CreateView):                           #create class for add post page
    model = post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields='__all__'                                    #import all form model[title,author,body,....]
    #field=('title','body')                              #import some form model
    success_url= reverse_lazy('home') 



class UpdatePostView(UpdateView):                       #create class for update post page
    model= post
    form_class = UpdateForm                             #import all from updateform
    template_name = 'update_post.html'
    #fields = ['title','author','body']
    success_url= reverse_lazy('home') 



class DeletePostView(DeleteView):                        #create class for delete post page
    model=post                                           #import all from POST MODEL
    template_name = 'delete_post.html'
    #fields = ['title','author','body']                    #import all fields from POST MODEL

    
    success_url= reverse_lazy('home')                        #make a reverser page 



class AddCategoryView(CreateView):                      #create class for add category page
    
    form_class = CategoryForm                           #import all from categoryform
    template_name = 'add_category.html'                 #import all from add_category.html
    


def CategoryView(request,cats):
    category_posts=post.objects.filter(category=cats)
    return render(request,'categories.html',{"cats":cats.title(),"category_posts":category_posts})


def cat_list(request):
    cat_list=Category.objects.all()
    return render(request,'base.html',{"cat_li" : cat_list})


