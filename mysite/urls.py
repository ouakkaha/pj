from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from main.views import about, blog
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', blog, name='blog'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]