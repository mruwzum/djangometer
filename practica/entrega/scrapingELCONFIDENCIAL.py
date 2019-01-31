# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import os.path
from practica.settings import HTML_DIR


def getWithBeautiful():

        webUrl = "https://www.elconfidencial.com/espana/"
        if not os.path.exists(HTML_DIR+"elconfidencialEspana.html"):
                urllib.request.urlretrieve(webUrl,HTML_DIR+"elconfidencialEspana.html")
        
        resultado = []  
        file = open(HTML_DIR+"elconfidencialEspana.html",encoding='utf8',mode="r")
        a = file.read()
        soup = BeautifulSoup(a, 'html.parser')
        # Sacamos los elementos del articulo
        listabloques = soup.select("article")   
        #     print(listabloques)
        i = 0    
        
        for bloque in listabloques:
                resultadoFor = ()
                if i is 0:
                        print("Sacando el articulo destacado")
                        titulohtml = bloque.find_all('a', class_=lambda x: x and x.startswith('archive-article-top-link'))
                        if titulohtml:
                                tituloNoticia = titulohtml[0].text
                                enlaceNoticia = titulohtml[0].get('href')
                        else:
                                tituloNoticia = " "
                                enlaceNoticia = "#"
                        descripcionHtml = bloque.find_all('h3', class_=lambda x: x and x.startswith('archive-article-top-leadin-tit'))
                        if descripcionHtml:
                                descripcionNoticia = descripcionHtml[0].text
                        else:
                                descripcionNoticia = " "     
                        
                        autorHtml = bloque.find_all('span', class_=lambda x: x and x.startswith('archive-article-top-author sig-color'))
                        if autorHtml:
                                autorNoticia = autorHtml[0].text
                        else:
                                autorHtml = " "
                        
                        comentariosHtml = bloque.find_all('em')
                        if comentariosHtml:
                                comentariosNoticia = comentariosHtml[0].text
                        else:
                                comentariosNoticia = " "
                        
                        
                        fechaHtml = bloque.find_all('meta', itemprop=lambda x: x and x.startswith('datePublished'))
                        if fechaHtml:
                                fechaNoticia = fechaHtml[0].text
                        else:
                                fechaNoticia = " "
                        
                        tupla = (tituloNoticia,enlaceNoticia,autorNoticia,comentariosNoticia,fechaNoticia)
                        resultadoFor = tupla

                else:
                        print("Sacando el resto de noticias")
                        titulohtml = bloque.find_all('h1', class_=lambda x: x and x.startswith('archive-article-tit'))
                        if titulohtml:
                                tituloNoticia = titulohtml[0].text
                        else:
                                tituloNoticia = " "

                        enlaceHtml = bloque.find_all('a', class_=lambda x: x and x.startswith('archive-article-link'))
                        if enlaceHtml:
                                enlaceNoticia = enlaceHtml[0].get('href')
                        else:
                                enlaceNoticia = "#"

                        descripcionHtml = bloque.find_all('h3', class_=lambda x: x and x.startswith('archive-article-leadin-tit'))
                        if descripcionHtml:
                                descripcionNoticia = descripcionHtml[0].text
                        else:
                                descripcionNoticia = " "   
                        
                        autorHtml = bloque.find_all('span', class_=lambda x: x and x.startswith('archive-article-author sig-color'))
                        if autorHtml:
                                autorNoticia = autorHtml[0].text
                        else:
                                autorHtml = " "

                        comentariosHtml = bloque.find_all('em')
                        if comentariosHtml:
                                comentariosNoticia = comentariosHtml[0].text
                        else:
                                comentariosNoticia = " "
                        
                        fechaHtml = bloque.find_all('meta', itemprop=lambda x: x and x.startswith('datePublished'))
                        if fechaHtml:
                                fechaNoticia = fechaHtml[0].text
                        else:
                                fechaNoticia = " "

                        tupla = (tituloNoticia,enlaceNoticia,autorNoticia,comentariosNoticia,fechaNoticia)
                        resultadoFor = tupla

                resultado.append(resultadoFor)
                i = i + 1  
        return resultado
         

