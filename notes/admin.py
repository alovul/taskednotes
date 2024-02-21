from django.contrib import admin
from .models import Notelist, User, Note

admin.site.register(Notelist)
admin.site.register(User)
admin.site.register(Note)
