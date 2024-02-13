from django.urls import path
from notes import views
from notes.models import Notelist



urlpatterns = [
    path("", views.home, name="home"),
    path("notes/", views.create_note_list, name="create_note_list"),
]