"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', blog_views.about, name='blog-about'),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('profile/', users_views.profile, name='profile'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)