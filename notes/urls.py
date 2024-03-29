from django.urls import path
from notes.views import home, signup, login, logged_out, addnotelist, addnote, delete_note, delete_notelist, addphotonote, images, delete_photonote, addtask, addtasklist, delete_task, delete_tasklist
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path('login/', LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logged_out/', LogoutView.as_view(template_name='notes/logged_out.html'), name='logged_out'),
    path("addnotelist/", addnotelist, name="addnotelist"),
    path('addnote/<int:note_list_id>/', addnote, name='addnote'),
    path('delete_notelist/<int:notelist_id>/', delete_notelist, name='delete_notelist'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    path('delete_photonote/<int:photonote_id>/', delete_photonote, name='delete_photonote'),
    path('addphotonote/', addphotonote, name='addphotonote'),
    path('images/', images, name='images'),
    path("addtasklist/", addtasklist, name="addtasklist"),
    path('addtask/<int:task_list_id>/', addtask, name='addtask'),
    path('delete_tasklist/<int:tasklist_id>/', delete_tasklist, name='delete_tasklist'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
