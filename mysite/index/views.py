from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"index.html")

def test(req):
    return render(req,"test.html")