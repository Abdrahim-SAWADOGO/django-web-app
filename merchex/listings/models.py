from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
   

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