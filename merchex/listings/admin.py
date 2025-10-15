from django.contrib import admin
from .models import Band, Listing

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['name']  # Colonnes affichées dans la liste
    search_fields = ['name']  # Champ de recherche

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'band_name']  # Affiche le titre et le band
    list_filter = ['band']  # Filtre par band
    search_fields = ['title']  # Recherche par titre

