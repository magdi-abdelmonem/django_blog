
from django.urls import path,reverse_lazy

from .views import Profile, User_profile, UserRegisterView,Edit_proff,Create_profile
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('register',UserRegisterView.as_view(),name='register'),
    path('creation_profile',Create_profile.as_view(),name='creation_profile'),
    path('<int:pk>/edit_profile',Edit_proff.as_view(), name='edit_profile'),
    path('profile/<int:pk>',Profile.as_view(),name='profile'),
    path('/<int:pk>/profile/',User_profile.as_view(),name='user_profile'),
    path('password/',auth_views.PasswordChangeView.as_view(
        template_name='registration/change_password.html',
        success_url = reverse_lazy('home') ),name='password')
]
    
  
