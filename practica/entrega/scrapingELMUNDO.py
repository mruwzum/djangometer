# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import os.path

from practica.settings import HTML_DIR




def getWithBeautiful(): 
		webUrl = "https://www.elmundo.es/espana.html"
		if not os.path.exists(HTML_DIR+"elmundoEspana.html"):
			urllib.request.urlretrieve(webUrl, HTML_DIR+"elmundoEspana.html")
		
		resultado = []
		
		
		file = open(HTML_DIR+"elmundoEspana.html",encoding='latin-1',mode="r")
		a = file.read()
		soup = BeautifulSoup(a, 'html.parser')
		# Sacamos los elementos del articulo
		listabloques = soup.select("article") 
		i = 0 
		for bloque in listabloques:      
			dirdocs = "practica/entrega/elmundoEspana"

			if i in range(0,2):
				# Elementos de cabecera
				tituloHtml = bloque.find_all('a', itemprop=lambda x: x and x.startswith('url'))
				if tituloHtml:
							tituloNoticia = tituloHtml[0].text
							enlaceNoticia = tituloHtml[0].get('href')
				else:
							tituloNoticia = " "   
							enlaceNoticia = "#"
				autorHTML = bloque.find_all('span', itemprop=lambda x: x and x.startswith('name'))
				if autorHTML:
							autorNoticia = autorHTML[0].text
				else:
							autorNoticia = " "   

				comentariosHTML = bloque.find_all('a', href=lambda x: x and x.startswith(enlaceNoticia +'#ancla_comentarios'))
				if comentariosHTML:
							comentariosNoticiaLista = comentariosHTML[0].text.split()
							comentariosNoticia = comentariosNoticiaLista[0]
				else:
							comentariosNoticia = "0"  

				fechaHtml = bloque.find_all('meta', itemprop=lambda x: x and x.startswith('datePublished'))
				if fechaHtml:
						fechaNoticia = fechaHtml[0].get('content')
				else:
						fechaNoticia = " "   
				tupla = (tituloNoticia, enlaceNoticia, autorNoticia, comentariosNoticia, fechaNoticia)
				resultado.append(tupla)

			elif(i in range(3,7)):
				#Resto de elementos
				tituloHtml = bloque.find_all('a', class_=lambda x: x and x.startswith('flex-article__heading-link'))
				if tituloHtml:
							tituloNoticia = tituloHtml[0].text
							enlaceNoticia = tituloHtml[0].get('href')
				else:
							tituloNoticia = " "   
							enlaceNoticia = "#"

				autorHTML = bloque.find_all('span', itemprop=lambda x: x and x.startswith('name'))
				if autorHTML:
							autorNoticia = autorHTML[0].text
				else:
							autorNoticia = " "

				comentariosHTML = bloque.find_all('a', href=lambda x: x and x.startswith(enlaceNoticia +'#ancla_comentarios'))
				if comentariosHTML:
							comentariosNoticiaLista = comentariosHTML[0].text.split()
							comentariosNoticia = comentariosNoticiaLista[0]
				else:
							comentariosNoticia = "0"  

				fechaHtml = bloque.find_all('meta', itemprop=lambda x: x and x.startswith('datePublished'))
				if fechaHtml:
						fechaNoticia = fechaHtml[0].get('content')
				else:
						fechaNoticia = " "   
				tupla = (tituloNoticia, enlaceNoticia, autorNoticia, comentariosNoticia, fechaNoticia)
				resultado.append(tupla)

			else:

				tituloHtml = bloque.find_all('a', itemprop=lambda x: x and x.startswith('url'))
				if tituloHtml:
							tituloNoticia = tituloHtml[0].text
							enlaceNoticia = tituloHtml[0].get('href')
				else:
							tituloNoticia = " "   
							enlaceNoticia = "#"   
				
				autorHTML = bloque.find_all('span', itemprop=lambda x: x and x.startswith('name'))
				if autorHTML:
							autorNoticia = autorHTML[0].text
				else:
							autorNoticia = " " 

				comentariosHTML = bloque.find_all('a', href=lambda x: x and x.startswith(enlaceNoticia +'#ancla_comentarios'))
				if comentariosHTML:
							comentariosNoticiaLista = comentariosHTML[0].text.split()
							comentariosNoticia = comentariosNoticiaLista[0]
				else:
							comentariosNoticia = "0"  
				fechaHtml = bloque.find_all('meta', itemprop=lambda x: x and x.startswith('datePublished'))
				if fechaHtml:
						fechaNoticia = fechaHtml[0].get('content')
				else:
						fechaNoticia = " "    
				tupla = (tituloNoticia, enlaceNoticia, autorNoticia, comentariosNoticia, fechaNoticia)
				resultado.append(tupla)

			i = i + 1
        
		return resultado
# 
if __name__ == "__main__":
    getWithBeautiful()