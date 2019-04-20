from django.shortcuts import render,get_object_or_404
from .models import posts
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
    )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

'''def home(request):
    Posts = posts.objects.all().order_by('-date_posted')
    context = {
        'Posts': Posts,
    }
    return render(request, 'blog/home.html', context)'''
    
class home(ListView):
    model = posts
    template_name = 'blog/home.html'
    context_object_name='Posts'
    ordering = '-date_posted'
    paginate_by = 3
    
class userpostlistview(ListView):
    model = posts
    template_name = 'blog/userposts.html'
    context_object_name='Posts'
    ordering = '-date_posted'
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return posts.objects.filter(author=user).order_by('-date_posted')

class createpost(LoginRequiredMixin ,CreateView):
    model = posts
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class updatepost(LoginRequiredMixin , UserPassesTestMixin,UpdateView):
    model = posts
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    


class Postdetailview(DetailView):
    model = posts

class deletepostview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = posts
    success_url='/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  
        


        

