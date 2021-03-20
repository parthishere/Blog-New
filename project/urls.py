"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


from blog import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', views.PostListView.as_view(), name='list-cbv'),
    path('drafts/', views.DraftListView.as_view(), name='draft-cbv'),
    
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='detail-cbv'),
    path('post/create', views.CreatePostView.as_view(), name='create'),
    path('post/publish/<int:pk>', views.publish_button, name='publish'),
    
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='update'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
    path('about/', views.about, name='about'),
    path('accounts/login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # path('comment/create', views.create_comments, name='comment'),
    # path('comment/delete/<int:pk>', views.delete_comment, name='del-comment'),
]
