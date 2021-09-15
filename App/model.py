"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from sys import call_tracing
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime as date
from DISClib.Utils import error as error


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog() : 
    """
    Inicializa el catálogo de los videos. Crea una lista para los videos y otra para las categorias. 
    """
    catalog = {'artWorks':None, 'categoria':None}
    catalog['artWorks'] = lt.newList('ARRAY_LIST')
    catalog['artista'] = lt.newList('ARRAY_LIST')
    catalog['categoria'] = lt.newList('ARRAY_LIST') 
    return catalog 

# Funciones para agregar informacion al catalogo
def addVideo (catalog, video): 
    """ #TODO:Documentacion.
    Para cada video, se añade al catalogo, se extrae el artista y ... 
    """
    lt.addLast(catalog['videos'],video)
    artistas =  video['ConstituentID'].split(',')
    for artista in artistas : 
        addArtists(catalog, artista.strip(), video)
    

def addArtists (catalog,artistas,video): 
    """
    #TODO:Documentacion. 
    """
    artists = catalog['ID Artista']
    posartist = lt.isPresent(artistas, artists)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else : 
        artist = newArtist(artistas)
        lt.addLast(artist, artists)
    lt.addLast(artist['video'],video)


# Funciones para creacion de datos
def newArtist(name): 
    """
    #TODO:Documentacion. 
    """
    artist = {'nombre':'','videos': None}
    artist['nombre'] = name 
    artist['videos'] = lt.newList('ARRAY_LIST')
    return artist 

# Funciones requerimiento 1

def compareartists(artist1, artist):
    if (artist1['ConstituendID'] == artist['ConstituendID']):
        return 0
    return -1

def compareratings(artist1, artist2):
    return (float(artist1['BeginDate']) > float(artist2['BeginDate']))

def sortArtist(catalog):
    sa.sort(catalog['artist'], compareratings)

def listCronoArtist(anioinicial,aniofinal,catalog):
    datosartist = lt.newList("ARRAY_LIST")
    stop = False
    i = 1
    while i <= lt.size(catalog["artist"]) and not stop:
        artist = lt.getElement(catalog["artist"],i)
        if anioinicial <= artist["BeginDate"] and artist["BeginDate"] <= aniofinal:
            lt.addLast(datosartist,artist)
        elif artist["BeginDate"] > aniofinal:
            stop = True
        i += 1
    return datosartist


# Funciones requerimiento 2

def cmpArtworkByDateAcquired(artwork1,artwork2):
    fechaObraA = date.date(int(artwork1["DateAcquired"].split("-")[0]),int(artwork1["DateAcquired"].split("-")[1]),int(artwork1["DateAcquired"].split("-")[2]))
    fechaObraB = date.date(int(artwork2["DateAcquired"].split("-")[0]),int(artwork2["DateAcquired"].split("-")[1]),int(artwork2["DateAcquired"].split("-")[2]))
    return (fechaObraA < fechaObraB)

def sortDate(catalog):
    sa.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

def listCronoAcquired(fechainicial,fechafinal,catalog):
    datosart = lt.newList("ARRAY_LIST")
    stop = False
    i = 1
    while i <= lt.size(catalog["Artworks"]) and not stop:
        obra = lt.getElement(catalog["Artworks"],i)
        if fechainicial <= obra["DateAcquired"] and obra["DateAcquired"] <= fechafinal:
            lt.addLast(datosart,obra)
        elif obra["DateAcquired"] > fechafinal:
            stop = True
        i += 1
    return datosart

# Función Sublist()

def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')


# ALGORITMOS DE ORDENAMIENTO

# Insertion sort

def insertionsort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpfunction(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst


# Shell sort

def shellsort(lst, cmpfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpfunction(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst


# Merge sort

def mergesort(lst, cmpfunction):
    size = lt.size(lst)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lst, 1, mid)
        rightlist = lt.subList(lst, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sort(leftlist, cmpfunction)
        sort(rightlist, cmpfunction)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpfunction(elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(lst, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lt.changeInfo(lst, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lst, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lst, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return lst


# Quick sort

def partition(lst, lo, hi, cmpfunction):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if cmpfunction(
           lt.getElement(lst, leader), lt.getElement(lst, hi)):
            lt.exchange(lst, follower, leader)
            follower += 1
        leader += 1
    lt.exchange(lst, follower, hi)
    return follower


def quicksort(lst, lo, hi, cmpfunction):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lst, lo, hi, cmpfunction)
    quicksort(lst, lo, pivot-1, cmpfunction)
    quicksort(lst, pivot+1, hi, cmpfunction)


def sort(lst, cmpfunction):
    quicksort(lst, 1, lt.size(lst), cmpfunction)
    return lst


