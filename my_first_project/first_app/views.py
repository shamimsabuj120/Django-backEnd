from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    diction ={'text_1':'I am a text sent from views.py file'}
    return render(request,'first_app/index.html', context=diction)
    # return HttpResponse("<h1> I am from first App </h1><a href='contact/'>contact</a> <a href='about/'>about</a>")

def contact(request):
    return HttpResponse("<h1> This is contact Page</h2> <a href='/about/'>about</a> <a href='/'>homepage</a>")

def about(request):
    return HttpResponse("<h1> this is about page</h1> <a href='/contact/'>contact</a> <a href='/'>homepage</a>")

