from django.shortcuts import render, redirect
from .models import Person
from django.http import HttpResponse, HttpResponseRedirect

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_item(request):
    if request.method == "POST":
        email = request.POST['email']
        picture = request.FILES['picture']
        # print(image)
        # print(description)
        person = Person(email=email, picture=picture)
        person.save()
        return redirect('email')
    else:
        return render(request, 'home.html')


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sherrykamath@gmail.com']
    # send_mail( subject, message, email_from, recipient_list )
    email = EmailMessage('Subject', 'Body', email_from, recipient_list)
    email.send()
    return render(request, 'home.html')