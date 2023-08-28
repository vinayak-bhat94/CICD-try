from django.urls import path
from . import views
urlpatterns = [
    path("route/", views.getRoutes,name="route"),
    path("notes/", views.getNotes,name="notes"),
    path("notes/create/", views.createNote,name="create"),
    path("notes/<str:pk>/", views.getNote,name="note"),
    path("notes/update/<str:pk>/", views.updateNote,name="update"),
    path("notes/delete/<str:pk>/", views.deleteNote,name="delete"),
    
]