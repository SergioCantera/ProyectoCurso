from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):    # Primera vista

    persona1 = Persona("Sergio", "Fonseca")
    
    #nombre = "Sergio"

    #apellido = "García"

    temas = ["Plantillas", "Vistas", "Modelos"]

    dias = {"1": "Lunes", "2": "Martes", "3": "Jueves"} 

    ahora = datetime.datetime.now()

    #doc_externo = open("C:/Users/Sergio/OneDrive/Documents/ProyectosDjango/ProyectoCurso/ProyectoCurso/templates/miplantilla.html")
    
    #plt = Template(doc_externo.read())

    #doc_externo.close()
    #doc_externo = get_template("miplantilla.html")

    #ctx = Context({"persona": persona1, "fecha": ahora, "temas": temas, "dias": dias})

    #documento = doc_externo.render({"persona": persona1, "fecha": ahora, "temas": temas, "dias": dias})

    return render(request, "miplantilla.html", {"persona": persona1, "fecha": ahora, "temas": temas, "dias": dias})

def despedida(request):
    
    return HttpResponse("Hasta luego, nos vemos pronto")

def dame_fecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales: %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, agno, edad):

    periodo = agno - 2020
    edad_futura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno, edad_futura)

    return HttpResponse(documento)