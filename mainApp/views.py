from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from mainApp.models import *


def home_view(request):
    return render(request, 'index.html')


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)


def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'kitoblar.html', context)


def bolimlar_view(request):
    bolimlar = Bolim.objects.all()
    context = {
        'bolimlar': bolimlar,
    }
    return render(request, 'bolimlar.html', context)
