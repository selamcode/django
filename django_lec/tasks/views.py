from django import forms # this will allow us to create forms
from django.http import HttpResponseRedirect # this will allow us to redirect the user to another page
from django.shortcuts import render # this will allow us to render the html file
from django.urls import reverse # this will allow us to get the url pattern for the index page


# Create your views here.

 

# tasks = [] # this is a list of tasks, if session exit we dont need this

class NewTaskForm(forms.Form): # this will allow us to create a form

    # create a form that will be used in the add.html file

    # label is the name of the field that will be displayed in the html file

    task = forms.CharField(label="New Task") # this is the label that will be displayed in the html file

    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=3) # this is the label that will be displayed in the html file



def index(request):
    if "tasks" not in request.session: # if the tasks key is not in the sessions dictionary then we will add it
        request.session["tasks"] = []

    # when we create the mapping "tasks":tasks the one inside the "" is used in the html file and the one after the : is the one we are passing in from here
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]  # this is the list of tasks we created above                                             
    })

def add(request):

    # if the action of the form is POST then we will create a new form with the data that was submitted

    if request.method == 'POST': # when submitting a form the method is always POST
         
        # requet.post is the data that was submitted
        form = NewTaskForm(request.POST)

        if form.is_valid():

            # if the form is valid then we will get the data from the form and add it to the tasks list
            # form.cleaned_data  will give access to all the data that was submitted
            # we need the task key because that is the name of the field in the form

            task = form.cleaned_data["task"]

            # add the task to the tasks list
            request.session["tasks"] += [task] # this is the same as tasks.append(task) but we are using 
                                        # sessions to store the data so people can see different tasks per session

            # if we don't have the code below we have to manually go to the index page to see the new task added
            # but with the code below we will be redirected to the index page and we will see the new task added

            # reverse is a built in function that will return the url pattern for the index page   
            return HttpResponseRedirect(reverse("tasks:index"))
        
        else:   
            # else if  the form is not valid then we will render the add.html page again with the form
            return render(request, "tasks/add.html", {
                "form": form
            })

            
    # else if the action of the form is GET then we will render the add.html page with the form
    return render(request, "tasks/add.html", {
       "form": NewTaskForm() # this is the form we created above
    })
