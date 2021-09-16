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
    catalog = {'Artists': None,'Artistas': None, 'ArtWorks': None}
    catalog['Artists'] = lt.newList('ARRAY_LIST')
    catalog['Artistas'] = lt.newList('ARRAY_LIST')
    catalog['ArtWorks'] = lt.newList('ARRAY_LIST')
    return catalog 

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist): 
    lt.addLast(catalog['Artists'],artist)
    artistas = artist['Artistas'].split(",")
    for artista in artistas : 
        addArtWorks(catalog,artista.strip(),artist)

def addArtWorks(catalog,artista, artist):
    artistas = catalog['Artistas']
    posartista = lt.isPresent(artistas, artista)
    if posartista > 0:
        nombreArtist = lt.getElement(artistas, posartista)
    else:
        nombreArtist = newArtist(artista)
        lt.addLast(artistas, nombreArtist)
    lt.addLast(nombreArtist['Artist'], artist)

def addArtWork(catalog, artwork):
    lt.addLast(catalog['ArtWorks'],artwork)
    obras = artwork['ArtWorks'].split(",") 


# Funciones para creacion de datos
def newArtist(name): 
    artist = {'nombre':'','Artworks': None}
    artist['nombre'] = name 
    artist['Artworks'] = lt.newList('ARRAY_LIST')
    return artist 

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

def compareobras(obra1,obra2):
    fechaObraA = date.date(int(obra1["DateAcquired"].split("-")[0]),int(obra1["DateAcquired"].split("-")[1]),int(obra1["DateAcquired"].split("-")[2]))
    fechaObraB = date.date(int(obra2["DateAcquired"].split("-")[0]),int(obra2["DateAcquired"].split("-")[1]),int(obra2["DateAcquired"].split("-")[2]))
    return (fechaObraA > fechaObraB)
        