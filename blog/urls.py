from django.urls import path
from  . import views  

urlpatterns = [
    path('', views.allblogs, name='allBlogs'),
    path('<int:blog_id>/', views.details, name ='detail')

] 