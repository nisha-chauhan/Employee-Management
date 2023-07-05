from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    print("test function is called from view")

    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"home.html",{})

def about(request):
   return render(request,"about.html",{})

def service(request):
    return render(request,"services.html",{})