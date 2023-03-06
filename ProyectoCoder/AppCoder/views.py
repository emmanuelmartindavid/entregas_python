from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso


def guardar_curso(request):
    curso = Curso(nombre="Python", camada=23800)
    curso.save()
    return HttpResponse("Usuario creado con exito")
