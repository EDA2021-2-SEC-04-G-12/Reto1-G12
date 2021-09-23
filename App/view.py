﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras por técnicas del artista")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Función de ordenamiento laboratorio 3")

def initCatalog(listType): 
    return controller.initCatalog(listType)
def loadData(catalog) : 
    controller.loadData(catalog)

def listArtworkbyDate (fecha_inicial, fecha_final,catalog) : 
    return controller.listArtworkbyDate(fecha_inicial, fecha_final,catalog)
def rankbyCountry(catalog) : 
    controller.rankbyCountry(catalog)

#Funciones de print 

def printSortResults(ord_artist, sample=10):
    size = lt.size(ord_artist)
    if size > sample:
        print("Los primeros ", sample, "libros ordenados son: ")
        i=1
        while i <= sample:
            book = lt.getElement(ord_artist,i)
            print("Object ID: "+artistas["ObjectID"]+" Título: "+artistas["Title"]
            +" Nombre del artista: "+artistas["ArtistsNames"]+" Medio: "+artistas["Medium"]
            +" Dimensiones: "+artistas["Dimensions"]+" Fecha: "+artistas["Date"]
            +" Fecha adquisición: "+artistas["DateAcquired"]+" URL: "+artistas["URL"])
            i+=1

def printArtistData(catalog, artists):
    artist = artists[0]
    total_obras = artists[1]
    total_tecnicas = artists[2]
    tecnica_mas_utilizada = artists[3]
    lista_obras_tecnica = artists[4]
    if artists != None:
        print(artist['DisplayName']+' with MoMA ID '+artist['ConstituentID']+'has'+ str(total_obras) +' pieces in his/her name at the museum.')
        print("There are " + str(total_tecnicas) + " different mediums/techniques in his/her work.")
        if tecnica_mas_utilizada != "":
            print("His/Her most used Medium/Techique is: " + str(tecnica_mas_utilizada))
        else: 
            print ("No tiene técnicas")
        if lt.size(lista_obras_tecnica) >= 1:
            print(lista_obras_tecnica["Title"] + lista_obras_tecnica["Date"] + lista_obras_tecnica["Medium"] + lista_obras_tecnica["Dimensions"])
        else:
            print("No tiene obras")
    
def printArtWork(artWork): 
    print("ObjectID: " + artWork['ObjectID'] + '\t|\t' + "ArtistID: " + artWork['ConstituentID'] + '\t|\t' + "Date: " + artWork['Date'] + "\t|\t" + artWork['Medium'] + "\t|\t" + artWork['Dimensions'])



catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        listType = int(input("Elija un tipo de lista para cargar los datos (1.ARRAY_LIST o 2.SINGLE_LINKED):"))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(listType) 
        loadData(catalog)
        print('Obras cargadas:  ' + str(lt.size(catalog['artWork'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artista'])))\

    elif int(inputs[0]) == 2:
        anioinicial = int(input("Ingrese el año inicial: "))
        aniofinal = int(input("Ingrese el año final: "))
        artistas = controller.listCronoArtist(anioinicial,aniofinal,catalog)
        print("Para el requerimiento 1, el tiempo (mseg) es: ", str(artistas[1]))
        tamanio = lt.size(artistas[0])
        print("\nHay "+ str(tamanio) + " artistas nacidos entre "+ str(anioinicial) + " y " + str(aniofinal))
        print("-"*50+"\n")
        print("Primeros 3: \n") 
        for i in range(1,4) : 
            artista = lt.getElement(artistas[0],i)
            print( "ConstituentID: " +artista['ConstituentID'] + "\t|\t" + "DisplayName: " + artista['DisplayName'] + "\t|\t" + "BeginDate: " + artista['BeginDate'] + "\t|\t" + "ArtistBio: " + artista['ArtistBio'] + "\t|\t"\
            + "Wiki QID: " + artista['Wiki QID'] + "\t|\t" + "ULAN: " +  artista['ULAN'] +'\n') 
        print("-"*50+"\n")
        print("\nUltimos 3: \n")
        for i in range(tamanio-3,tamanio+1) : 
            artista = lt.getElement(artistas[0],i)
            print( "ConstituentID: " +artista['ConstituentID'] + "\t|\t" + "DisplayName: " + artista['DisplayName'] + "\t|\t" + "BeginDate: " + artista['BeginDate'] + "\t|\t" + "ArtistBio: " + artista['ArtistBio'] + "\t|\t"\
            + "Wiki QID: " + artista['Wiki QID'] + "\t|\t" + "ULAN: " +  artista['ULAN'] +'\n')

    elif int(inputs[0]) == 3: 
        fecha_inicial = input("Fecha inicial(AAAA-MM-DD): ")
        fecha_final = input("Fecha final(A1AAA-MM-DD): ")
        result = listArtworkbyDate(fecha_inicial,fecha_final,catalog)
        print("El numero total de obras en el rango especificado es: " + str(lt.size(result[0]))) 
        print("El numero de obras adquiridas por compra es: " + str(result[1]))
        print('Las ultimas 3 obras en el rango son: \n')
        for i in range(lt.size(result[0])-3,lt.size(result[0])): 
            artwork = lt.getElement(result[0],i) 
            printArtWork(artwork) 
        print("\n" +"Las primeras 3 obras son: \n")
        for i in range(1,4):
            artwork = lt.getElement(result[0],i) 
            printArtWork(artwork)
    
    elif int(inputs[0]) == 4:
        artistname = input("Nombre del artista a buscar: ")
        artists = controller.getArtworksArtist(artistname, catalog)
        print(artists)
        if artists != None:
            print("Para el requerimiento 3, el tiempo (mseg) es: " + str(artists[5]))
            printArtistData(catalog, artists)
        else:
            print('No se encontro el artista')

    elif int(inputs[0]) == 5:
        print('Clasificando obras...') 
        result = rankbyCountry(catalog) 


    elif int(inputs[0]) == 7:
        size = int(input("Indique tamaño de la muestra: "))
        orden = int(input("Indique un número para seleccionar un ordenamiento específico: (1) Insertion Sort  (2) Shell Sort  (3) Merge Sort  (4) Quick Sort\n"))
        result = controller.sortArtists(catalog, int(size),int(orden))
        print("Para la muestra de", size, " elementos en el requerimiento 2, el tiempo (mseg) es: ",
                                          str(result[0]))
        printSortResults(result[1])


    else:
        sys.exit(0)
sys.exit(0)
