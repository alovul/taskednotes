from django.contrib import admin
from .models import Notelist, User, Note, Photonote

admin.site.register(Notelist)
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Photonote)
