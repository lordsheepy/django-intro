from django.contrib import admin
from django.core.urlresolvers import reverse
from photoshare.models import Photo
from photoshare.models import Album
from photoshare.models import Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'owner_link', 'created', 'height', 'width')

    def owner_link(self, photo):
        url = reverse('admin:auth_user_change', args=(photo.id,))
        name = photo.owner
        return '<a href="%s">%s</a>' % (url, name)
    owner_link.allow_tags = True


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_link')

    def owner_link(self, album):
        url = reverse('admin:auth_user_change', args=(album.id,))
        name = album.owner
        return '<a href="%s">%s</a>' % (url, name)
    owner_link.allow_tags = True

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
