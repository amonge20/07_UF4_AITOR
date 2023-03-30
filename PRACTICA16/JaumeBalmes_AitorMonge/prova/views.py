from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def prof(request):
    professor = {"name": "Aitor", "surname": "Monge", "age": 22}

    return render(request, 'prof.html', {'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})

def users(request):
    alumn = {"name": "Kevin", "surname": "Sama", "age": 18}

    return render(request, 'users.html', {'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})