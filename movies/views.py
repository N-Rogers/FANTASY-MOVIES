from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from movies.forms import categoryform, movieform
from movies.models import moviecategory
from .models import movie
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import DetailView
# Create your views here.

def moviehome(request):
    files = movie.objects.all().order_by('-created')
    context = {
        'files':files
    } 
    return render(request, 'movies/home.html', context)

def createmoviecategory(request):
    
    if request.method == 'POST':
        form = categoryform(request.POST)
        if form.is_valid():
            form.save()

            return redirect('moviehome')
    else:
        form = categoryform()  
        return render(request, 'movies/category.html', {'form': form})    
    
def moviecatlist(request):
    list = moviecategory.objects.all()
    content = {
        'list':list
    }
    return render(request,'movies/moviecatlist.html',content )

def search(request):
    query = request.GET.get('q')

    if query:
        results = movie.objects.filter(Q(movie_title__icontains=query))

    context={
        'files':results
    }
    return render(request,'movies/home.html',context )


def createmovie(request):
    if request.method == 'POST':
        form = movieform(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('moviehome')
    else:
        form = movieform()
        return render(request, 'movies/movieform.html', {'form': form})

def getactionmovie(request):
    files = movie.objects.filter(category__name="Action").order_by('-created')
    context = {
        'files':files
    }
    return render(request, 'movies/home.html', context)

def getadveturemovie(request):
    files = movie.objects.filter(category__name="Adventure").order_by('-created')
    context = {
        'files':files
    }
    return render(request, 'movies/home.html', context)    

def playmovie(request, movie_id):
    play_movie = get_object_or_404(movie, pk=movie_id)
    files = movie.objects.all()
    allmovies = movie.objects.filter(Q(category__name=play_movie.category))
         
    context = {
        'play_movie': play_movie,
        'allmovies':allmovies,
    }
    return render(request, 'movies/movie_detail.html', context)

