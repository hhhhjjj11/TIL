from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField(blank=True, null=True)
    release_data = models.DateField(blank=True,null=True )
    genre_Choice = (('Comedy','Comedy'),('Romance','Romance'),('Horror','Horror'))
    genre = models.CharField(max_length=30, choices=genre_Choice)
    score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    poster_url = models.CharField(blank=True,max_length=50)
    description = models.TextField(blank=True,null=True)
    actor_image = models.ImageField(blank=True,null=True)