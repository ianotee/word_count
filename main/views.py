from django.shortcuts import render




def base(request):
    return render(request, "base.html")

def home(request):

    name = " Word Counter"
    return render(request, "home.html", {"name": name})

def counter(request):
    text  = request.POST["text"]
    amount = len(text.split())
    count = "The Word count is"
    calc = "THE WORD CALCULATOR"
    return render(request, "counter.html", {"amount":amount,"count":count,"calc":calc})
