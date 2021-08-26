from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def second_url(request):
    return render(request, "index2.html")


def second_url2(request):
    return render(request, "index3.html")


def second_url3(request):
    return render(request, "index4.html")
