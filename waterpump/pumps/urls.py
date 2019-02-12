from django.urls import path
from . import views

app_name = "pumps"
urlpatterns = [
    path("", view=views.Feed.as_view(), name='feed'),
    path("cities/", view=views.ListAllCities.as_view(), name="cities"),
    path("towns/", view=views.ListAllTowns.as_view(), name="towns"),
    path("sectors/", view=views.ListAllSectors.as_view(), name="sectors"),
    path("pumps/", view=views.ListAllPumps.as_view(), name="pumps"),

]
