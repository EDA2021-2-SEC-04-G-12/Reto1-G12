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
 """

from time import thread_time
import config as cf
import model
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime as date 
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(listType): 
    if listType == 1: 
        TADlist = 'ARRAY_LIST'
    elif listType == 2: 
        TADlist = 'SINGLE_LINKED'
    catalog = model.newCatalog(TADlist) 
    return catalog 

# Funciones para la carga de datos
def loadData(catalog): 
    loadartWork(catalog)
    loadArtists(catalog)

def loadartWork(catalog): 
    artWorkfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artWorkfile, encoding='utf-8'))
    for video in input_file :
        model.addartWork(catalog,video)

def loadArtists(catalog): 
    """
    #TODO:DOCUMENTACION 
    """
    artistsfile = cf.data_dir +'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artista in input_file:
        model.addArtists_2(catalog, artista)

# Funciones de ordenamiento

def sortArtists(catalog, size, orden):
    return model.sortArtists(catalog, size, orden)
    
def listArtworkbyDate (fecha_inicial, fecha_final,catalog) : 
    fecha_A = date.datetime.strptime(fecha_inicial,'%Y-%m-%d')
    fecha_B = date.datetime.strptime(fecha_final,'%Y-%m-%d')
    artWorks = model.listArtworkbyDate(fecha_A, fecha_B,catalog)
    Cuenta_purchase = model.countPurchasedArtwork(artWorks)
    return artWorks,Cuenta_purchase 

def listCronoArtist(anioinicial,aniofinal,catalog):

    return model.listCronoArtist(anioinicial,aniofinal,catalog)

# Funciones de consulta sobre el catálogo

def getArtworksArtist(artist_name, catalog):
    artist = model.getArtworksArtist(artist_name, catalog)
    return artist


def countArtworks(artwork, catalog):
    return model.countArtworks(artwork, catalog)