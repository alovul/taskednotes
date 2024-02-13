from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from notes.forms import CreateNoteListForm  
from notes.models import Notelist

def home(request):
    return render(request, 'home.html')

def create_note_list(request):
    if request.method == 'POST':
        form = CreateNoteListForm(request.POST)
        if form.is_valid():
            # Process the form data (save the new note list, etc.)
            # Assuming your CreateNoteListForm has a save() method to handle saving the form data
            form.save()
            # Redirect to a success page or any other page you desire
            return redirect('home')  # Redirect to the home page after creating a note list
    else:
        form = CreateNoteListForm()

    return render(request, 'notes/create_note_list.html', {'form': form})