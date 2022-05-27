from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,LikeView

urlpatterns = [

    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/delete/<int:pk>',DeletePostView.as_view(), name='delete_post'),
    path('category',AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>',CategoryView, name='category_view'),
    path('like/<int:pk>',LikeView, name='like_post'),

]