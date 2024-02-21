from django import forms
from notes.models import Notelist, User, Note
from django.contrib.auth.forms import UserCreationForm

class CreateNoteListForm(forms.ModelForm):
    class Meta:
        model = Notelist
        fields = ["name",]   # NOTE: the trailing comma is required

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['description',]