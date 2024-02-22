from django.contrib import admin
from .models import Notelist, User, Note, Photonote, Task, Tasklist

admin.site.register(Notelist)
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Photonote)
admin.site.register(Task)
admin.site.register(Tasklist)

