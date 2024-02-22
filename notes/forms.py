from django import forms
from notes.models import Notelist, User, Note, Photonote, Task, Tasklist
from django.contrib.auth.forms import UserCreationForm

class CreateNoteListForm(forms.ModelForm):
    class Meta:
        model = Notelist
        fields = ["name",]   # NOTE: the trailing comma is required

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs.update({'accept': 'image/*'})

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['description',]

class AddPhotoNoteForm(forms.ModelForm):
    class Meta:
        model = Photonote
        fields = ['name', 'description', 'image']

class AddTaskListForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ["name",]

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'completed']