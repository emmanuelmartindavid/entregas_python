from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def mostrar_html(request):
    return HttpResponse("<button>mi boton</button><h1>Hello world")


def retornar_parametros(request):
    mensaje = f"La fecha de hoy es: {datetime.now()}"
    return HttpResponse(mensaje)


def mi_nombre(request, nombre):
    return HttpResponse(f"Hello. Welcome <b>{nombre}</b>")


def show_html(request):
    return render(request, "template1.html")


def show_html2(request, cursada):
    contexto = {
        "cursada": cursada,
        "entidad": "coder",
        "fecha": datetime.now(),
        "lista": [1, 2, 3, 4 , 5],
        "diccionario":{
            "nombre": "Emma",
            "apellido": "Martin"
        }
    }
    return render(request, "template2.html", context=contexto)
