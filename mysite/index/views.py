from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"content1.html")