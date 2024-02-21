from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)

class Notelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    
    def delete_notes(self):
        # Delete all notes associated with this note list
        Note.objects.filter(note_list=self).delete()


    def __str__(self):
        return f"{self.user.username}'s {self.name}"

class Note(models.Model):
    note_list = models.ForeignKey(Notelist, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Note in {self.note_list}: {self.description}"

class Photonote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='img')

    def delete_photonotes(self):
        # Delete all notes associated with this note list
        Photonote.objects.filter(photonote=self).delete()

    def __str__(self):
        return f"{self.user.username}'s {self.name}"