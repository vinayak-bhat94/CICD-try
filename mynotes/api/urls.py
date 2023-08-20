from django.urls import path
from . import views
urlpatterns = [
    path("route/", views.getRoutes,name="route"),
    path("notes/", views.getNote,name="note"),
]