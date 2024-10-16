from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"content1.html")

def test(req):
    return render(req,"test.html")