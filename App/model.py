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


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog() : 
    """
    Inicializa el catálogo de los videos. Crea una lista para los videos y otra para las categorias. 
    """
    catalog = {'videos':None, 'categoria':None}
    catalog['Videos'] = lt.newList('ARRAY_LIST')
    catalog['ID artista'] = lt.newList('ARRAY_LIST')
    catalog['Artista'] = lt.newList('ARRAY_LIST')
    catalog['Categoria'] = lt.newList('ARRAY_LIST') 
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


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento