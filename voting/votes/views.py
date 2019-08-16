from django.shortcuts import render
from .models import Person
from django.http import HttpResponse, HttpResponseRedirect
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