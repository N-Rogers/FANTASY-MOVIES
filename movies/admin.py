from django.contrib import admin
from .models import (movie, moviecategory)

# Register your models here.
admin.site.register(movie)
admin.site.register(moviecategory)
