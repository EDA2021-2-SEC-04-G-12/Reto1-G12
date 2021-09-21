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


from csv import DictReader
from sys import call_tracing
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as quic
assert cf
import datetime as date
from DISClib.Utils import error as error
import time


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(listType) : 
    """
    Inicializa el catálogo de los videos. Crea una lista para los videos y otra para las categorias. 
    """
    catalog = {'artWork':None, 'categoria':None}
    catalog['artWork'] = lt.newList(listType)
    catalog['artista'] = lt.newList(listType,compareartists)
    catalog['categoria'] = lt.newList(listType) 
    return catalog 

# Funciones para agregar informacion al catalogo

def addartWork (catalog, artWork): 
    """ #TODO:Documentacion.
    Para cada video, se añade al catalogo, se extrae el artista y ... 
    """
    lt.addLast(catalog['artWork'],artWork)
    artistas = catalog["artista"].split(",")
    for artista in artistas:
        addArtists_2(catalog, artista.strip())
    
def addArtists_2 (catalog, artist): 
    """
    Adiciona un artista a la lista de artistas. 
    """
    a = newArtist_2(artist['DisplayName'],artist['ConstituentID'],artist['ArtistBio'],\
        artist['Nationality'],artist['Gender'],artist['BeginDate'],artist['EndDate'],\
            artist['Wiki QID'],artist['ULAN']) 
    lt.addLast(catalog['artista'],a)


# Funciones para creacion de datos

def newArtist_2(DisplayName,id,bio,nationality,gender,begin,end,wiki,ulan): 
    """
    Esrta estructura almacena los datos de los artistas. 
    """
    artista = {'DisplayName': '', 'ConstituentID':''}
    artista['DisplayName'] = DisplayName 
    artista['ConstituentID'] = id 
    artista['ArtistBio'] = bio 
    artista['Nationality'] = nationality
    artista['Gender'] = gender
    artista['BeginDate'] = begin
    artista['EndDate'] = end
    artista['Wiki QID'] = wiki 
    artista['ULAN'] = ulan 
    return artista


# Funciones requerimiento 1

def compareartists(artist1, artista):
    if (artist1.lower() in artista['DisplayName'].lower()):
        return 0
    return -1

def compareratings(artist1, artist2):
    return (float(artist1['BeginDate']) > float(artist2['BeginDate']))

def sortArtist(catalog):
    sa.sort(catalog['artist'])

def listCronoArtist(anioinicial,aniofinal,catalog):
    datosartist = lt.newList("ARRAY_LIST")
    stop = False
    i = 1
    while i <= lt.size(catalog["artista"]) and not stop:
        artist = lt.getElement(catalog["artista"],i)
        if anioinicial >= int(artist["BeginDate"]) and int(artist["BeginDate"]) <= aniofinal:
            lt.addLast(datosartist,artist)
        elif int(artist["BeginDate"]) > aniofinal:
            stop = True
        i += 1
    return datosartist



# Funciones requerimiento 2

def cmpArtworkByDateAcquired(artwork1,artwork2):
    fechaObraA = date.date(int(artwork1["DateAcquired"].split("-")[0]),int(artwork1["DateAcquired"].split("-")[1]),int(artwork1["DateAcquired"].split("-")[2]))
    fechaObraB = date.date(int(artwork2["DateAcquired"].split("-")[0]),int(artwork2["DateAcquired"].split("-")[1]),int(artwork2["DateAcquired"].split("-")[2]))
    return (fechaObraA < fechaObraB)

def sortDateInsertion(catalog):
    ins.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

def sortDateShell(catalog):
    sa.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

def sortDateMerge(catalog):
    mer.sort(catalog['Artworks'], cmpArtworkByDateAcquired) 

def sortDateQuick(catalog):
    quic.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

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

def sortArtists(catalog, size, orden):
    sub_list = lt.subList(catalog['artWork'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    if orden == 1:
        sorted_list = ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif orden == 2:
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif orden == 3:
        sorted_list = mer.sort(sub_list, cmpArtworkByDateAcquired)
    elif orden == 4:
        sorted_list = quic.sort(sub_list, cmpArtworkByDateAcquired)
    return elapsed_time_mseg, sorted_list


# Funciones requerimiento 3

def getArtworksArtist(artist, catalog):
    posartist = lt.isPresent(catalog['artista'], artist)
    if posartist > 0:
        artist = lt.getElement(catalog['artista'], posartist)
        return artist
    return None

def countArtworks(artwork, catalog):
    artworks = catalog['artWork']
    artworkcount = 0
    pos = lt.isPresent(artworks, artwork)
    if pos > 0:
        artwork_element = lt.getElement(artworks, pos)
        if artwork_element is not None:
            for artwork_artist in lt.iterator(catalog['artWork']):
                if artwork_element['ConstituentID'] == artwork_artist['ConstituentID']:
                    artworkcount += 1
    return artworkcount