"""
URL configuration for django_firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
"""yani folder se wo file import kro"""
from django_firstproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about-us/',views.about_us),
    # path('courses/',views.courses),
    # """dynamic routing"""
    
    # path('courses/<int:courseid>',views.courseDetail),
    
    # path('courses/<str:courseid>',views.courseDetail),
    
    # path('courses/<slug:courseid>',views.courseDetail),
    
    # """if u have ni idea about type then not use any type"""
    
    # path('courses/<courseid>',views.courseDetail),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('products/',views.products,name="products"),
    path('userform/',views.userform,name="userform"),
    path('categories/',views.categories,name="categories"),
    path('transfer/',views.transfer,name="transfer"),
    path('register/',views.register,name="register"),
    path('news_detail/<newsid>',views.news_detail,name="news_detail"),
    
    
]

