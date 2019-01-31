# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import os.path

from practica.settings import HTML_DIR




def getWithBeautiful(): 
    webUrl = "https://elpais.com/politica/"
    if not os.path.exists(HTML_DIR+"elpaisEspana.html"):
        urllib.request.urlretrieve(webUrl,HTML_DIR+"elpaisEspana.html")

    i = 1
    resultado = []
    
    
    file = open(HTML_DIR+"elpaisEspana.html",encoding='utf-8',mode="r")
    a = file.read()
    soup = BeautifulSoup(a, 'html.parser')
    # Sacamos los elementos del articulo
    listabloques = soup.select("article")   
    i = 1    
    
    for bloque in listabloques:
            dirdocs = "practica/entrega/elpaisEspana"


            linkHtml = bloque.find_all('h2', class_=lambda x: x and x.startswith('articulo-titulo'))
            #print(link)


            #print(link)
            for elem in linkHtml:
                titulo = elem.text
                link = elem.a.get('href')
            
            autorHtml = bloque.find_all('span', class_=lambda x: x and x.startswith('autor-nombre'))
            #print(link)

            #print(link)
            for elem in autorHtml:
                autor = elem.a.text
            

            comentarioHtml = bloque.find_all('span', class_=lambda x: x and x.startswith('articulo-comentarios'))
            
            #print(link)
            for elem in comentarioHtml:
                comentarios = elem.text
            

            fechaHtml = bloque.find_all('meta', itemprop=lambda x: x and x.startswith('datePublished'))
            
            #print(link)
            for elem in fechaHtml:
                fecha = elem.get('content')[0:10]
            
            file.close()
            i = i + 1
            # FORMATO DE SALIDA DE LA LISTA DE TUPLAS temas : tema(ID,titulo,link,fecha,respuestas,visitas,autor) 
            tupla = (titulo, link, autor, comentarios ,fecha)
            resultado.append(tupla)    
    return resultado


if __name__ == "__main__":
   a = getWithBeautiful()
   