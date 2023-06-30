from django.urls import path

from . import views # the dot means current folder


#  "" default basically signiviews the app name http://127.0.0.1:8000/hello thats why we did empty string
""" our default page is http://127.0.0.1:8000/hello
    now if we want to add another page that says hello selam we do path( "selam", the the view function)
"""
# <str:name> bsically means "wheni have a string variable name"

urlpatterns = [
    
    path("", views.hello_world),
    path("selam", views.selam, name = "selam"),
    path("<str:name>", views.greet, name = "greet")  
]