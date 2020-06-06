from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request , 'generator/home.html')
def password(request):
    character = list('abcdefghijklmnopqrstuvwxy')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXZ'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(character)
    return render(request , 'generator/password.html', {'password':thepassword})

def aboutus(request):
    return render(request, 'generator/aboutus.html')
