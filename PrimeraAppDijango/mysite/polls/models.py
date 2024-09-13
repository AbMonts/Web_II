from django.db import models

# Modelo para el estudio de animación
class Studio(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modelo para los géneros de anime
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    episodes = models.IntegerField()

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # Ejemplo: Protagonista, Antagonista

    def __str__(self):
        return self.name

# Modelo para las reseñas de los usuarios
class Review(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()  # Ejemplo: Escala de 1 a 10
    comment = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user_name} on {self.anime}'
