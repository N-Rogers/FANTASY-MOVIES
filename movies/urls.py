from django.urls import path
from . import views

urlpatterns = [
    path('', views.moviehome, name='moviehome'),
    path('results/', views.search,name='search'),
    path('moviecat/', views.createmoviecategory, name='category'),
    path('moviecatlist/', views.moviecatlist, name='categorylist'),
    path('createmovie/', views.createmovie, name='movie-create'),
    path('actiomovies/', views.getactionmovie, name='action-movies'),
    path('adventuremovies/', views.getadveturemovie, name='adventure-movies'),
    path('<int:movie_id>/', views.playmovie, name='playmovie'),
   
]