from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def bootcamp(request):
    return render(request,'bootcamp.html')