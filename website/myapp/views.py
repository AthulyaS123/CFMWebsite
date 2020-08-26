from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    return render(request, 'homepage.html')
def aboutus(request):
     return render(request, 'aboutuspage.html')
def blog(request):
    return render(request, 'blogpage.html')