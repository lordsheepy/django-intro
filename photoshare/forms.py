from django.forms import ModelForm
from photoshare.models import Album, Photo, Tag


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['name']


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'comment']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
