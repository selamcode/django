from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()

    # here we have a newyear string varibale mapped to now.day == 1 and now.month == 1, inside the index.html we will check
    # if year newyear True or False when index return the render function.
    
    return render(request, "newyear/index.html", {
         "newyear" : now.day == 1 and now.month == 1
        }
    )

