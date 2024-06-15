from django.contrib import admin
from .models import Club, Drill, User, Event, Calendar

# Register your models here.

admin.site.register(User)
admin.site.register(Club)
admin.site.register(Drill)
admin.site.register(Event)
admin.site.register(Calendar)
