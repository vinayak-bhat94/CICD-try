from django.urls import path
from . import views
urlpatterns = [
    path("route/", views.getRoutes,name="route"),
    path("notes/", views.getNotes,name="notes"),
    path("notes/<str:pk>/", views.getNote,name="note"),
]