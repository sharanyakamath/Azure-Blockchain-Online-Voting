from django.shortcuts import render
from .models import Person
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import base64
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.files import File

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

        with open("test.png", "wb") as fh:
            temp = base64.decodebytes(str.encode(picture.split("base64,")[1]))
            fh.write(temp)

        person = Person(username=username, picture=picture)
        person.save()
        return HttpResponseRedirect('/votes/home')
    else:
        return render(request, 'pic.html')

def index(request):
    if request.POST:
        # give the absolute path to your `text4midiAllMilisecs.py`
        # and for `tiger.mid`
        # subprocess.call(['python', '/path/to/text4midiALLMilisecs.py', '/path/to/tiger.mid'])

        subprocess.call('/home/palak/CodeFunDo19/voting/votes/run_sh.sh')

    return render(request, 'home.html')
