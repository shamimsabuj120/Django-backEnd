from django.contrib import admin
from first_app.models import musician, album

# Register your models here.
admin.site.register(musician)
admin.site.register(album)