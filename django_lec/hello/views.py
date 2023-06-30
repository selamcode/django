from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# This function handles only the logice, the html design is inside html file good design!
def hello_world(request):
    return render (request, "hello/hello_world.html" ) 

# this function handels both logic and html together, for a bigger and organized project its considered a bad design
def selam(request):
    return HttpResponse("Hello Selam!" )  # return hello Selam

# This function handles only the logice, the html design is inside html file good design!
def greet(request, name):
    # the thirs parameter is a dictionary 
    return render(request, "hello/greet.html", {
    "name": "name".capitalize()
    })
