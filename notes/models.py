from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    profile_picture = models.ImageField(upload_to='img/profile_pictures/', blank=True, null=True)

    
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
    def delete(self, *args, **kwargs):
        # Delete the associated image file from the file system
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        # Call the parent class's delete method to delete the object from the database
        super().delete(*args, **kwargs)
    def __str__(self):
        return f"{self.user.username}'s {self.name}"

class Tasklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def delete_tasks(self):
        # Delete all tasks associated with this task list
        Task.objects.filter(task_list=self).delete()
    
    def __str__(self):
        return f"{self.user.username}'s {self.name}"

class Task(models.Model):
    task_list = models.ForeignKey(Tasklist, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task in {self.task_list}: {self.description}"
