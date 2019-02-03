from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import shuffle
import os
from .models import *
from .forms import *
import sqlite3
from difflib import SequenceMatcher
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FOLDER = os.path.join(BASE_DIR)
from igmeter.InstaMeter import *


# Just reads the results out of the dictionary. No real logic here.

def index(request):
    im = InstaMeter(username='elenabravoarche')
    im.analyze_profile()

    # listaResultado.append(im.print_top_liked())
    # listaResultado.append(im.print_top_commented())
    # listaResultado.append(im.print_top_viewed())
    context = {'res': im.print_account_statistic()}
    return render(request, 'igmeter/index.html',context)
# Create your views here.


# def noticias(request):
    
#     listaNoticias = Noticias.objects.all()

#     context = {'lista': listaNoticias}
    
#     return render(request, 'igmeter/noticias.html', context)


# def relevancia(request):
#     lista = []
#     lista = Noticias.objects.all()
    
#     resultado = []
#     for elem in lista:
#         aux = [elem.titulo, elem.link, elem.comentarios, elem.fecha, elem.idNoticia]
#         resultado.append(aux)
    
#     ordenado = sorted(resultado, key=lambda x: x[2])

#     ordenado = ordenado[len(ordenado)-3:]
    
#     for elem in ordenado:
#         print(elem[2])
    

#     aux = ordenado[0]
#     ordenado[0] = ordenado[2]
#     ordenado[2] = aux

    
#     context = {'lista': ordenado}
#     return render(request, 'igmeter/top3.html', context)




# def busqueda(request):
#     lista = Noticias.objects.all()

#     form = MovieForm(request.GET) #definiendo aquí el methodo request.GET se consigue el valor del formulario
#     busqueda = form['titulo'].value()

#     print(str(busqueda))

#     resultado = []

#     for elem in lista:
#         if str(busqueda) in elem.titulo:
#             aux = elem
#             resultado.append(aux)


#     context = {'lista': resultado, 'form':form}

#     return render(request, 'igmeter/search.html', context)

# def recomendadas(request):
#     noticia_id = 26
#     lista = recommend(noticia_id,5)
#     titular = lista[0]
#     lista.reverse()
#     lista.pop(5)
#     lista.reverse()
#     conn = sqlite3.connect(BASE_DIR + '/db.sqlite3')
#     cursor = conn.cursor()
#     listaDef = []
#     res = []
#     for elem in lista:
#         for row in cursor.execute('SELECT * FROM igmeter_noticias t where titulo == ?',[elem]):
#             listaDef.append(row)
#     context = {'lista': listaDef, "titular":titular}
#     return render(request, 'igmeter/recomienda.html', context)


# def recomendadasId(request,movie_id):
#     noticia_id = movie_id
#     lista = recommend(noticia_id,5)
#     titular = lista[0]
#     lista.reverse()
#     lista.pop(5)
#     lista.reverse()
#     conn = sqlite3.connect(BASE_DIR + '/db.sqlite3')
#     cursor = conn.cursor()
#     listaDef = []
#     res = []
#     for elem in lista:
#         for row in cursor.execute('SELECT * FROM igmeter_noticias t where titulo == ?',[elem]):
#             listaDef.append(row)
#     context = {'lista': listaDef, "titular":titular}
#     return render(request, 'igmeter/recomienda.html', context)   


# def cargar(request):
#     cargarDatos()
#     return render(request,'igmeter/cargarDic.html')