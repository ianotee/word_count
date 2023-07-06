from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt



def base(request):
    return render(request, "main/base.html")

def home(request):

    name = " Word Counter"
    return render(request, "main/home.html", {"name": name})

def counter(request):
    text  = request.POST["text"]
    amount = len(text.split())
    count = "The Word count is"
    calc = "THE WORD CALCULATOR"
    return render(request, "main/counter.html", {"amount":amount,"count":count,"calc":calc})
