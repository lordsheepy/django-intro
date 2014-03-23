from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login


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
        template_name='photoshare/login.html',)


def home_view(request):
    return render(request, 'photoshare/home.html')
