from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Using below class we can directly add HTML into web pages.
class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [] # Look inside sessions, if there is already a tasks. If not, create one. 


    return render(request,"tasks/index.html", {
        "tasks": request.session["tasks"]      #This is key value pair where key is "tasks" and value is tasks. The value tasks can be accessed in HTML created in tempates/tasks/index.html or any html using Jinja notations.
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)  # Contains all data that users submitted when they submitted the form. All data will be availabel in form variable.
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index")) # This will redirect to HTML page once tasks are added
        else:
            return (request, "tasks/add.html", {
                "form" : form
            })

    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })

