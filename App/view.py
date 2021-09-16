"""
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
    print("3- Ordenar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")

def initCatalog(): 
    return controller.initCatalog()

def loadData(catalog) : 
    controller.loadData(catalog)

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


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog() 
        loadData(catalog)
        print('Videoss cargados:  ' + str(lt.size(catalog['video'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artista'])))\



    elif int(inputs[0]) == 2:
        anioinicial = int(input("Ingrese el año inicial: "))
        aniofinal = int(input("Ingrese el año final: "))
        artistas = controller.listCronoArtist(anioinicial,aniofinal,catalog)
        print("Hay "+str(lt.size(catalog["artistas"])))

    elif int(inputs[0]) == 3:
        size = input("Indique tamaño de la muestra: ")
        orden = input("Indique un número para seleccionar un orden específico: (1) Insertion Sort  (2) Shell Sort  (3) Merge Sort  (4) Quick Sort\n")
        result = controller.sortArtists(catalog, int(size),int(orden))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printSortResults(result[1])
        

    else:
        sys.exit(0)
sys.exit(0)
