from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='photos',
        related_query_name='photo',
        )
    height = models.IntegerField(blank=True, null=True, default=0)
    width = models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(
        upload_to='%Y/%m/%d',
        height_field='height',
        width_field='width',
        )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=144, blank=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='photos',
        related_query_name='photo',
        )

    def __unicode__(self):
        return 'photo_id.' + unicode(self.pk)


class Album(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(
        User,
        related_name='albums',
        related_query_name='album',
        )
    photos = models.ManyToManyField(
        Photo,
        related_name='albums',
        related_query_name='album',
        blank=True,
        null=True,
        )

    def __unicode__(self):
        return self.name
