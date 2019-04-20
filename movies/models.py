from django.db import models

# Create your models here.

class moviecategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class movie(models.Model):
    category = models.ForeignKey(moviecategory, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=100)
    movie_file=models.FileField()
    istranslated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_title       
    
