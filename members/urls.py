from django.urls import path
from . import views
from .views import UserRegisterView,UserEditView,PasswordChangeView,ShowProfileView,EditProfileView,CreateProfileView,CustomLoginView
from django.contrib.auth import views as auth_views

from . import views
urlpatterns=[
    path('register/', views.register, name='register'),
    path('verify_otp/<str:email>/', views.verify_otp, name='verify_otp'),
    path('login/', CustomLoginView.as_view(), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    path('password/',PasswordChangeView.as_view(),name='password_change'),
    path('password_success/',views.password_success,name='password_success'),
    path('profile/<int:pk>',ShowProfileView.as_view(),name = 'show_profile'),
    path('noprofile',views.ShowProfile,name = 'no_profile'),
    path('edit_profile_page/<int:pk>',EditProfileView.as_view(),name = 'edit_profile_page'),
    path('create_profile_page/',CreateProfileView.as_view(),name = 'create_profile_page'),
]