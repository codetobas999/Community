from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    str = 'Welcome to MyPage'
    template = loader.get_template('index.html')
    context = {'var1': str}
    return HttpResponse(template.render(context, request))

def aboutus(request):
    str = 'This is about us'
    template = loader.get_template('aboutus.html')
    context = {'var2': str}
    return HttpResponse(template.render(context, request))

def contact(request):
    str = 'contact: test@abc.com'
    template = loader.get_template('contact.html')
    context = {'var3': str}
    return HttpResponse(template.render(context, request))
