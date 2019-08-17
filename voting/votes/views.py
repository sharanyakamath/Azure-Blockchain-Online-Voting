from django.shortcuts import render
from .models import Person
from django.http import HttpResponse, HttpResponseRedirect
import subprocess
# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_item(request):
    if request.method == "POST":
        username = request.POST['username']
        picture = request.FILES['picture']
        # print(image)
        # print(description)
        person = Person(username=username, picture=picture)
        person.save()
        return HttpResponseRedirect('/votes/home')
    else:
        return render(request, 'home.html')

def index(request):
    if request.POST:
        # give the absolute path to your `text4midiAllMilisecs.py`
        # and for `tiger.mid`
        # subprocess.call(['python', '/path/to/text4midiALLMilisecs.py', '/path/to/tiger.mid'])

        subprocess.call('/home/palak/CodeFunDo19/voting/votes/run_sh.sh')

    return render(request, 'home.html')