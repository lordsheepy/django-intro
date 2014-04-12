from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from photoshare.forms import AlbumForm, PhotoForm, TagForm, EditPhotoForm
import models



def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def front_view(request):
    return render(request, 'photoshare/front.html')


def login_view(request):
    request.next = 'photoshare/home'
    return login(
        request,
        template_name='registration/login.html',)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required
def home_view(request):
    albums = models.Album.objects.filter(owner=request.user).all()
    context = {'albums': albums}
    return render(request, 'photoshare/home.html', context)


@login_required
def album_view(request, album):
    album = models.Photo.objects.filter(album=album).all()
    context = {'album': album}
    return render(request, 'photoshare/album.html', context)


@login_required
def photo_view(request, photo):
    photo = models.Photo.objects.get(pk=photo)
    context = {'photo': photo}
    return render(request, 'photoshare/photo.html', context)


@login_required
def tag_view(request, tag):
    photos = models.Photo.objects.filter(owner=request.user).filter(tags=tag).all()
    context = {'photos': photos, 'tag': tag}
    return render(request, 'photoshare/tag.html', context)


@login_required
def add_album_view(request):
    if request.method == "POST":
        album = models.Album(owner=request.user)
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/photoshare/home/')
    context = {
        'page': 'photoshare.views.add_album_view',
        'button': 'Add Album',
        'form': AlbumForm,
    }
    return render(request, 'photoshare/add_view.html', context)


@login_required
def add_photo_view(request):
    if request.method == "POST":
        photo = models.Photo(owner=request.user)
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/photoshare/home/')
    else:
        form = PhotoForm()
        form.fields['album'].queryset = models.Album.objects.filter(
            owner=request.user).all()

    context = {
        'page': 'photoshare.views.add_photo_view',
        'button': 'Add Photo',
        'form': form,
    }
    return render(request, 'photoshare/add_view.html', context)


@login_required
def add_tag_view(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect()
    context = {
        'page': 'photoshare.views.add_tag_view',
        'button': 'Add Tag',
        'form': TagForm,
    }
    return render(request, 'photoshare/add_view.html', context)


@login_required
def edit_photo_view(request, photo_id):
    photo = models.Photo.objects.get(pk=photo_id)
    if request.method == "POST":
        form = EditPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/photoshare/home/photo/'+photo_id)
    else:
        form = EditPhotoForm(instance=photo)
        form.fields['album'].queryset = models.Album.objects.filter(
            owner=request.user).all()

    context = {
        'id': photo_id,
        'button': 'Edit Photo',
        'form': form,
    }
    return render(request, 'photoshare/edit_photo.html', context)
