from django.shortcuts import render
from .models import Person
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import base64
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files import File
import os


import subprocess
# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_item(request):
    if request.method == "POST":
        print('Hi')
        username = request.POST['username']
        picture = request.FILES['picture']

        person = Person(username=username, picture=picture)
        person.save()
        return HttpResponseRedirect('/votes/home')
    else:
        return render(request, 'home.html')

@csrf_exempt
def pic(request):
    if request.method == "POST":
        username = request.POST['username']
        picture = request.POST['picture']
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR+'/unknown_people/', username + ".png") 
        with open(file_path, "wb") as fh:
            temp = base64.decodebytes(str.encode(picture.split("base64,")[1]))
            fh.write(temp)

        person = Person(username=username, picture=picture)
        person.save()
        return HttpResponseRedirect('/votes/home')
    else:
        return render(request, 'pic.html')

def index(request):
    if request.POST:
        subprocess.call('./votes/run_sh.sh')
        with open('out', 'r') as file:
            f = file.read().replace('\n', '')
        print("ksk")
        print(f)
        if f== "0":
            return render(request, 'home.html')
        else:
            return render(request, 'verify.html')
    else:
        return render(request, 'verify.html')

def verify(request):
    return render(request, 'verify.html')
