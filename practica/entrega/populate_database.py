from datetime import datetime
import entrega.scrapingELCONFIDENCIAL as elConfidencial
import entrega.scrapingELPAIS as elPais
import entrega.scrapingELMUNDO as elMundo
import sqlite3
import os
from entrega.models import Noticias, Autor


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cargarDatos():

    print(" ")
    print("Borrando base de datos previa")
    conn = sqlite3.connect(BASE_DIR + '/db.sqlite3')
    cursor = conn.cursor()
    dropTableStatement = 'DELETE FROM entrega_autor'
    dropTableStatement2 = 'DELETE FROM entrega_noticias'
    cursor.execute(dropTableStatement)
    cursor.execute(dropTableStatement2)
    conn.commit()
    conn.close()

    print(" ")
    print("Realizando la migración. Esta operación puede tardar unos minutos.")
    print(" ")
    tuplas = elConfidencial.getWithBeautiful()
    #print(tuplas)
    for elem in tuplas:
        a, created = Autor.objects.get_or_create(nombre = elem[2])



    i = 0
    for elem in tuplas:
        
        tituloM = elem[0].replace(",",".").replace("\n","")
        enlaceM = elem[1]
        autorM = elem[2]
        autorM = str(autorM).replace('.', "")
        comentariosM = elem[3]
        fechaM = elem[4]
        if(fechaM is ""):
            fechaM=datetime.now()
        try:
            g, created = Noticias.objects.get_or_create(titulo = tituloM, link = enlaceM, autor= autorM,comentarios=comentariosM, fecha= fechaM)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


    tuplas = elPais.getWithBeautiful()
    #print(tuplas)
    for elem in tuplas:
        c, created = Autor.objects.get_or_create(nombre = elem[2])


    for elem in tuplas:
        try:
            d, created = Noticias.objects.get_or_create(titulo = elem[0].replace(",",".").replace("\n",""), link = elem[1], autor= elem[2],comentarios=elem[3], fecha= elem[4])
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


    tuplas = elMundo.getWithBeautiful()
    #print(tuplas)
    for elem in tuplas:
        e, created = Autor.objects.get_or_create(nombre = elem[2])


    for elem in tuplas:
        fechaM = elem[4]
        if(fechaM is ' ' or fechaM is ''):
            fechaM=datetime.now()
        try:
            f, created = Noticias.objects.get_or_create(titulo = elem[0].replace(",",".").replace("\n",""), link = elem[1], autor= elem[2],comentarios=elem[3], fecha= fechaM)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


