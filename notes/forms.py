from django import forms
from notes.models import Notelist

class CreateNoteListForm(forms.ModelForm):
    class Meta:
        model = Notelist
        fields = ("name",)   # NOTE: the trailing comma is required