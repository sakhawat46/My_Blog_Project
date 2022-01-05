from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('', views.BlogList.as_view(), name='blog_list'),
    path('details/<str:slug> ', views.blog_details, name='blog_details'),
    path('liked/<pk>', views.liked, name='liked'),
    path('unliked/<pk>', views.unliked, name='unliked'),
    path('my-blogs/',views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(),name='edit_blog'),
]  