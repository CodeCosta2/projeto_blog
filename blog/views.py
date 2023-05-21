from django.shortcuts import render


def my_home(request):
    return render(request, "blog/home.html")


def my_about(request):
    return render(request, "blog/about.html")
