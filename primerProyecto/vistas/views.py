from django.http import HttpResponse
import datetime
from django.template import Template, Context

class personas():
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


# creando primera vista
def saludo(request):
    # cargando una plantilla
    p1 = personas('Ing. Hamel', 'Zabala')

    #nombre = 'Hamel'
    #apellido = 'Zabala'
    fecha_hoy = datetime.datetime.now()

    doc_externo = open(r'C:\Users\HP PROBOOK\OneDrive\Desktop\django.py\primerProyecto\primerProyecto\plantillas\mi_plantilla.html')
    
    plt = Template(doc_externo.read())

    doc_externo.close()

    # creando un diccionario dentro de Context para usar esa informacion en mi plantilla
    ctx = Context({"mi_nombre": p1.nombre, "mi_apellido": p1.apellido, "fecha": fecha_hoy})

    documento = plt.render(ctx)

    return HttpResponse(documento)

# vista de despedida
def despedida(request):
    hora_actual = datetime.datetime.now().time()

    #cargando el documento html
    cargando_doc = open(r'C:\Users\HP PROBOOK\OneDrive\Desktop\django.py\primerProyecto\primerProyecto\plantillas\despedida.html')

    # leyendo lo que dentro del documento html    
    plt = Template(cargando_doc.read())

    cargando_doc.close() # cerrando la conexion
    
    ctx = Context({"hora": hora_actual})

    documento = plt.render(ctx)

    return HttpResponse(documento)


def calcula_edad(request, edad, anos):
    ano_actual = datetime.datetime.now().year
    periodo = anos - ano_actual
    edad_futura = edad + periodo

    cargando_doc = open(r'C:\Users\HP PROBOOK\OneDrive\Desktop\django.py\primerProyecto\primerProyecto\plantillas\calculandoEdad.html')
    
    plt = Template(cargando_doc.read())

    cargando_doc.close()

    ctx = Context({"edadActual": edad, "edadFutura": edad_futura, "anos": anos})

    documento = plt.render(ctx)
    
    return HttpResponse(documento)