from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout as auth_logout
from .forms import CreateNoteListForm, SignUpForm, AddNoteForm, AddPhotoNoteForm
from .models import Notelist, User, Note, Photonote
from django.contrib.auth.decorators import login_required

# Use LoginView and LogoutView for login and logout views
login = LoginView.as_view(template_name='notes/login.html')
logged_out = LogoutView.as_view(template_name='notes/logout.html')

@login_required
def home(request):
    # Retrieve all task lists for the logged-in user
    note_lists = Notelist.objects.filter(user=request.user)

    return render(request, 'notes/home.html', {'note_lists': note_lists})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'notes/signup.html', {'form': form})

def addnotelist(request):
    if request.method == 'POST':
        form = CreateNoteListForm(request.POST)
        if form.is_valid():
            notelist = form.save(commit=False)
            notelist.user = request.user  # Set the user
            notelist.save()
            return redirect("home")
    else:
        form = CreateNoteListForm()

    return render(request, 'notes/addnotelist.html', {'form': form})

def addnote(request, note_list_id):
    note_list = Notelist.objects.get(id=note_list_id)
    notes = Note.objects.filter(note_list=note_list)

    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.note_list = note_list
            note.save()
            return redirect('addnote', note_list_id=note_list_id)  # Updated redirection so that user can stay in add note page
    else:
        form = AddNoteForm()

    context = {
        'note_list_id': note_list_id,
        'form': AddNoteForm(),
        'notes': notes,
    }

    return render(request, 'notes/addnote.html', context)

def delete_notelist(request, notelist_id):
    notelist = get_object_or_404(Notelist, pk=notelist_id)
    if request.method == 'POST':
        notelist.delete_notes()  # Delete all notes that were in the list
        notelist.delete()
        return redirect('home')
    return render(request, 'notes/delete_notelist.html', {'notelist': notelist})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note_list_id = note.note_list.id 
    
    if request.method == 'POST':
        note.delete()
        return redirect('addnote', note_list_id=note_list_id)
    
    return render(request, 'notes/delete_note.html', {'note': note, 'note_list_id': note_list_id})

def addphotonote(request):

    if request.method == 'POST':
        form = AddPhotoNoteForm(request.POST, request.FILES)
        if form.is_valid():
            photonote = form.save(commit=False)
            photonote.user = request.user
            photonote.save()
            return redirect('images')
    else:
        form = AddPhotoNoteForm()
    
    return render(request, 'notes/addphotonote.html', {'form': form})

def images(request):
    photonotes = Photonote.objects.filter(user=request.user)
    return render(request, 'notes/images.html', {'photonotes': photonotes})

def delete_photonote(request, photonote_id):
    photonote = get_object_or_404(Photonote, pk=photonote_id)    
    if request.method == 'POST':
        photonote.delete()
        return redirect('images')
    
    return render(request, 'notes/delete_photonote.html', {'photonote': photonote})