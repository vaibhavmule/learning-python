from django.shortcuts import render

from .forms import ContactForm, SignUpForm
# Create your views here.

def contact(request):
    form = ContactForm
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def home(request):
    title = 'Welcome'
    form = SignUpForm()
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'home.html', context)

