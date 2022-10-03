from django.contrib import admin
from .models import Movie
# Register your models here.

class Movielist(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'rating')
    list_filter = ('name', 'year', 'description')
    search_fields = ('name', 'description')
    ordering = ['year']

admin.site.register(Movie, Movielist)