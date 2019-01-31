from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import shuffle
import os
from .models import Noticias
from .forms import *
import sqlite3
from difflib import SequenceMatcher
import pandas as pd
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FOLDER = os.path.join(BASE_DIR)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from entrega.populate_database import cargarDatos


# Just reads the results out of the dictionary. No real logic here.
def recommend(item_id, num):
    
    with open('file.csv', 'w+') as write_file:
        conn = sqlite3.connect(BASE_DIR + '/db.sqlite3')
        cursor = conn.cursor()
        write_file.write("id,description"+"\n")
        for row in cursor.execute('SELECT t.idNoticia, t.titulo FROM entrega_noticias t'):
            texto = row[1].replace(",",".")
            if ("\n" in texto):
                write_file.write(str(row[0])+","+texto[1:])
            else:
                write_file.write(str(row[0])+","+texto+ "\n")

    ds = pd.read_csv(CSV_FOLDER+"/file.csv")
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(ds['description'])
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    results = {}

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]
        results[row['id']] = similar_items[1:]
    
    
    
    resultado = []
    resultado.append("Recomendando " + str(num) + " artículos similares a: "  + item(item_id,ds))
    recs = results[item_id][:num]
    for rec in recs:
        print(item(rec[1],ds) + " (puntuación:" + str(rec[0]) + ")")
        resultado.append(item(rec[1],ds))
    return resultado

def item(id, ds):
    return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

def index(request):
    return render(request, 'entrega/index.html')
# Create your views here.


def noticias(request):
    
    listaNoticias = Noticias.objects.all()

    context = {'lista': listaNoticias}
    
    return render(request, 'entrega/noticias.html', context)


def relevancia(request):
    lista = []
    lista = Noticias.objects.all()
    
    resultado = []
    for elem in lista:
        aux = [elem.titulo, elem.link, elem.comentarios, elem.fecha, elem.idNoticia]
        resultado.append(aux)
    
    ordenado = sorted(resultado, key=lambda x: x[2])

    ordenado = ordenado[len(ordenado)-3:]
    
    for elem in ordenado:
        print(elem[2])
    

    aux = ordenado[0]
    ordenado[0] = ordenado[2]
    ordenado[2] = aux

    
    context = {'lista': ordenado}
    return render(request, 'entrega/top3.html', context)




def busqueda(request):
    lista = Noticias.objects.all()

    form = MovieForm(request.GET) #definiendo aquí el methodo request.GET se consigue el valor del formulario
    busqueda = form['titulo'].value()

    print(str(busqueda))

    resultado = []

    for elem in lista:
        if str(busqueda) in elem.titulo:
            aux = elem
            resultado.append(aux)


    context = {'lista': resultado, 'form':form}

    return render(request, 'entrega/search.html', context)

def recomendadas(request):
    noticia_id = 26
    lista = recommend(noticia_id,5)
    titular = lista[0]
    lista.reverse()
    lista.pop(5)
    lista.reverse()
    conn = sqlite3.connect(BASE_DIR + '/db.sqlite3')
    cursor = conn.cursor()
    listaDef = []
    res = []
    for elem in lista:
        for row in cursor.execute('SELECT * FROM entrega_noticias t where titulo == ?',[elem]):
            listaDef.append(row)
    context = {'lista': listaDef, "titular":titular}
    return render(request, 'entrega/recomienda.html', context)


def recomendadasId(request,movie_id):
    noticia_id = movie_id
    lista = recommend(noticia_id,5)
    titular = lista[0]
    lista.reverse()
    lista.pop(5)
    lista.reverse()
    conn = sqlite3.connect(BASE_DIR + '/db.sqlite3')
    cursor = conn.cursor()
    listaDef = []
    res = []
    for elem in lista:
        for row in cursor.execute('SELECT * FROM entrega_noticias t where titulo == ?',[elem]):
            listaDef.append(row)
    context = {'lista': listaDef, "titular":titular}
    return render(request, 'entrega/recomienda.html', context)   


def cargar(request):
    cargarDatos()
    return render(request,'entrega/cargarDic.html')