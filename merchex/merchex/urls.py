from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('band/',views.band,name='band'),
    path('about-us/',views.about,name='about'),
    path('',views.home,name='home'),
]
