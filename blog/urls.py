from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='bloghome'),
    path('createpost/',views.createpost.as_view(),name='create_post'),
    path('posts/<int:pk>/', views.Postdetailview.as_view(), name='postdetails'),
    path('posts/<int:pk>/update', views.updatepost.as_view(), name='updatepost'),
    path('posts/<int:pk>/delete',views.deletepostview.as_view(), name='deletepost'),
    path('userposts/<str:username>', views.userpostlistview.as_view(), name='userposts'),


]       