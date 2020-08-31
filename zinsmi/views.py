from django.shortcuts import render, redirect


# Create your views here.

def main(request):
    return render(request, 'mainpage.html')


def works(request):
    return render(request, 'works.html')


def us_page(request):
    return render(request, 'people.html')


def contacts(request):
    return render(request, 'contacts.html')