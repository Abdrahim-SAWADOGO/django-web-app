from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# listings/models.py

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50,default="")
    biography = models.fields.CharField(max_length=1000,default="")
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(now().year)],default=now().year
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
   

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    band = models.ForeignKey(
        Band,
        on_delete=models.CASCADE,
        related_name='listings'
        )
    @property
    def band_name(self):
        return self.band.name