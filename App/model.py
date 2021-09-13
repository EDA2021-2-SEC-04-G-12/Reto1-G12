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
    return (fechaObraA > fechaObraB)
        