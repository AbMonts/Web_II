from django.contrib import admin
from .models import Studio, Genre, Anime, Character, Review

# Registra los modelos en el admin
admin.site.register(Studio)
admin.site.register(Genre)
admin.site.register(Anime)
admin.site.register(Character)
admin.site.register(Review)
