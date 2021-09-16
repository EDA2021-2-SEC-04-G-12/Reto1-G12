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
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog() : 
    """
    Inicializa el catálogo de los videos. Crea una lista para los videos y otra para las categorias. 
    """
    catalog = {'artWork':None, 'categoria':None, 'ID artista':None, 'artista': None, 'categoria':None}
    catalog['artWork'] = lt.newList('ARRAY_LIST')
    catalog['ID artista'] = lt.newList('ARRAY_LIST')
    catalog['artista'] = lt.newList('ARRAY_LIST')
    catalog['artista_2'] = lt.newList('ARRAY_LIST')
    catalog['categoria'] = lt.newList('ARRAY_LIST') 
    return catalog 

# Funciones para agregar informacion al catalogo
def addartWork (catalog, artWork): 
    """ #TODO:Documentacion.
    Para cada video, se añade al catalogo, se extrae el artista y ... 
    """
    lt.addLast(catalog['artWork'],artWork)
    artistas =  artWork['ConstituentID'].split(',')
    for artista in artistas : 
        addArtists(catalog, artista.strip('[]'),artWork)
    

def addArtists (catalog,artista,artWork): 
    """
    . 
    """
    artists = catalog['ID artista']
    posartist = lt.isPresent(artists, artista)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else : 
        artist = newArtist(artista)
        lt.addLast(artists, artista)
    lt.addLast(artist['artWork'],artWork)

def addArtists_2 (catalog, artist): 
    """
    Adiciona un artista a la lista de artistas. 
    """
    a = newArtist_2(artist['DisplayName'],artist['ConstituentID'],artist['ArtistBio'],\
        artist['Nationality'],artist['Gender'],artist['BeginDate'],artist['EndDate'],\
            artist['Wiki QID'],artist['ULAN']) 
    lt.addLast(catalog['artista_2'],a)


# Funciones para creacion de datos
def newArtist(ID): 
    """
    #TODO:Documentacion. 
    """
    artist = {'nombre':None ,'artWork': None}
    artist['nombre'] = ID 
    artist['artWork'] = lt.newList('ARRAY_LIST')
    return artist 

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



# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento