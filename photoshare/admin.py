from django.contrib import admin
from photoshare.models import Photo
from photoshare.models import Album
from photoshare.models import Tag

# Register your models here.

admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(Tag)
