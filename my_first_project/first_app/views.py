from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import musician, album
from  first_app import forms

# Create your views here.
def index(request):
    #SQL SELECT * FROM musician ORDER BY firts_name
    musician_list = musician.objects.order_by('first_name')
    diction ={'text_1':'I am a text sent from views.py file & this is an musucian list', 'Musician':musician_list}
    return render(request,'first_app/index.html', context=diction)
    # return HttpResponse("<h1> I am from first App </h1><a href='contact/'>contact</a> <a href='about/'>about</a>")

def contact(request):
    return HttpResponse("<h1> This is contact Page</h2> <a href='/about/'>about</a> <a href='/'>homepage</a>")

def about(request):
    return HttpResponse("<h1> this is about page</h1> <a href='/contact/'>contact</a> <a href='/'>homepage</a>")

def form(request):
    new_form = forms.user_form()
    diction={'test_form':new_form, 'heading_1':"this form is created by django library"}
    return render(request,'first_app/form.html', context=diction)