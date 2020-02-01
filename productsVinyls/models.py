from django.db import models

# Create your models here.

# Models for Vinyl Products

class Vinyl(models.Model):
    artist = models.CharField(max_length=254, default='')
    album = models.CharField(max_length=254, default='')
    genre = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name