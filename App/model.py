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
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las 
categorias de los mismos.
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
    art = newartWork(artWork['ConstituentID'],artWork['Date'],artWork['Medium'],artWork['Dimensions'],artWork['CreditLine'],\
        artWork['AccessionNumber'],artWork['Classification'],artWork['Department'],artWork['DateAcquired'],artWork['Cataloged'],\
            artWork['ObjectID'],artWork['URL'],artWork['Circumference (cm)'],artWork['Depth (cm)'],artWork['Diameter (cm)'],artWork['Height (cm)'],\
                artWork['Length (cm)'],artWork['Weight (kg)'],artWork['Width (cm)'],artWork['Seat Height (cm)'],artWork['Duration (sec.)'])
    lt.addLast(catalog['artWork'],art)
    
def addArtists_2 (catalog, artist): 
    """
    Adiciona un artista a la lista de artistas. 
    """
    a = newArtist_2(artist['DisplayName'],artist['ConstituentID'],artist['ArtistBio'],\
        artist['Nationality'],artist['Gender'],artist['BeginDate'],artist['EndDate'],\
            artist['Wiki QID'],artist['ULAN']) 
    lt.addLast(catalog['artista'],a)


# Funciones para creacion de datos
def newartWork (ConstituentID,date,medium,dimensions,creditLine,accessionNumber,clasification,department,\
    dateAquired,Cataloged,objectId,URL,circumference,depth,diameter,height,length,weight,width,seatHeight,duration): 
    ArtWork = {'ConstituentID':'','Date':'','Medium':'','Dimensions':'','CreditLine':'','AccessionNumber':'',\
        'Classification':'','Department':'','DateAcquired':'','Cataloged':'','ObjectID':'','URL':'','Circumference':'',\
            'Depth':'','Diameter':'','Height':'','Length':'','Weight':'','Width':'','Seat Height':'','Duration':''}
    ArtWork['ConstituentID'] = ConstituentID
    ArtWork['Date'] = date
    ArtWork['Medium'] = medium
    ArtWork['Dimensions'] = dimensions
    ArtWork['CreditLine'] = creditLine
    ArtWork['AccessionNumber'] = accessionNumber
    ArtWork['Classification'] = clasification
    ArtWork['Department'] = department 
    ArtWork['DateAcquired'] = dateAquired
    ArtWork['Cataloged'] = Cataloged
    ArtWork['ObjectID'] = objectId
    ArtWork['URL'] = URL
    ArtWork['Circumference'] =circumference
    ArtWork['Depth'] = depth
    ArtWork['Diameter'] = diameter
    ArtWork['Height'] = height
    ArtWork['Length'] = length
    ArtWork['Weight'] = weight
    ArtWork['Width'] = width
    ArtWork['Seat Height'] = seatHeight
    ArtWork['Duration'] = duration
    return ArtWork


def newArtist_2(DisplayName,id,bio,nationality,gender,begin,end,wiki,ulan): 
    """
    Esrta estructura almacena los datos de los artistas. 
    """
    artista = {'DisplayName': '', 'ConstituentID':'','ArtistBio':'','Nationality':'','Gender':'','BeginDate':'',\
        'EndDate':'','Wiki QID':'','ULAN':''}
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
    start_time = time.process_time()
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    while i <= lt.size(catalog["artista"]) and not stop:
        artist = lt.getElement(catalog["artista"],i)
        if anioinicial >= int(artist["BeginDate"]) and int(artist["BeginDate"]) <= aniofinal:
            lt.addLast(datosartist,artist)
        elif int(artist["BeginDate"]) > aniofinal:
            stop = True
        i += 1
    return datosartist, elapsed_time_mseg



# Funciones requerimiento 2

def cmpArtworkByDateAcquired(artwork1,artwork2):
    cadena_fecha_A = artwork1['DateAcquired']
    cadena_fecha_B = artwork2['DateAcquired']
    if len(cadena_fecha_A) > 0 and len(cadena_fecha_B) > 0: 
        fecha_A = date.datetime.strptime(cadena_fecha_A,'%Y-%m-%d')
        fecha_B = date.datetime.strptime(cadena_fecha_B,'%Y-%m-%d')
        return fecha_A < fecha_B
    elif len(cadena_fecha_A) > 0 and len(cadena_fecha_B) == 0 : 
        return True
    elif len(cadena_fecha_A) == 0 and len(cadena_fecha_B) > 0 : 
        return False 


def sortDateInsertion(catalog):
    ins.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

def sortDateShell(catalog):
    sa.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

def sortDateMerge(catalog):
    mer.sort(catalog['Artworks'], cmpArtworkByDateAcquired) 

def sortDateQuick(catalog):
    quic.sort(catalog['Artworks'], cmpArtworkByDateAcquired)

def listArtworkbyDate(fechainicial,fechafinal,catalog):
    size= lt.size(catalog['artWork'])
    sortArtwork(catalog,2)
    datosart = lt.newList("ARRAY_LIST")
    stop = False
    i = 1
    while i <= size and not stop:
        obra = lt.getElement(catalog['artWork'],i)
        if len(obra['DateAcquired']) > 0 :
            fecha_obra  = date.datetime.strptime(obra['DateAcquired'],'%Y-%m-%d') 
            if fechainicial <= fecha_obra and fechafinal >= fecha_obra : 
                lt.addLast(datosart,obra) 
            elif fecha_obra > fechafinal : 
                stop = True 
        i += 1
    return datosart
def countPurchasedArtwork(artworks) : 
    """
    Cuenta el numero de obras adquiridas por purchase. 
    """
    size = lt.size(artworks)
    i = 1 
    count = 0 
    while i < size : 
        artwork = lt.getElement(artworks, i)
        if 'Purchase' in  artwork['CreditLine'] : 
            count += 1 
        i += 1 
    return count 
        
def sortArtwork(catalog,orden):
    if orden == 1:
      ins.sort(catalog['artWork'], cmpArtworkByDateAcquired)
    elif orden == 2:
      sa.sort(catalog['artWork'], cmpArtworkByDateAcquired)
    elif orden == 3:
      mer.sort(catalog['artWork'], cmpArtworkByDateAcquired)
    elif orden == 4:
      quic.sort(catalog['artWork'], cmpArtworkByDateAcquired)


# Funciones requerimiento 3

def cmpArtworks(artwork1, artwork2):
    return artwork1["Medium"] < artwork2["Medium"]

def getArtworksArtist(artist, catalog):
    posartist = lt.isPresent(catalog['artista'], artist)
    if posartist > 0:
        artworkartist = lt.newList()
        artist = lt.getElement(catalog['artista'], posartist)
        idartist = int(artist["ConstituentID"])
        i = 1
        while i <= lt.size(catalog["artWork"]):
            artwork = lt.getElement(catalog["artWork"], i)
            if idartist in artwork["ConstituentID"]:
                lt.addLast(artworkartist, artwork)
            i += 1
        sorted_list = quic.sort(artworkartist, cmpArtworks)
        j = 2
        count = 0
        mayor = 0
        count1 = 0
        name = ""
        while j <= lt.size(sorted_list):
            if lt.getElement(sorted_list, j)["Medium"] != lt.getElement(sorted_list, j-1)["Medium"]:
                count += 1
                if count1 > mayor:
                    mayor = count1
                    name = lt.getElement(sorted_list, j-1)["Medium"]
                count1 = 0
            else:
                count1 += 1
            j += 1

        return artist
    return None

#Funciones requerimiento 4
def sortArtists(catalog,orden) : 
    """
    Organiza los artistas por su ConstituentID 
    """
    if orden == 1:
      ins.sort(catalog['artista'], compareArtistbyID)
    elif orden == 2:
      sa.sort(catalog['artista'], compareArtistbyID)
    elif orden == 3:
      mer.sort(catalog['artista'], compareArtistbyID)
    elif orden == 4:
      quic.sort(catalog['artista'], compareArtistbyID)



def compareArtistbyID (artist1,artist2) : 
    ID_1 = int(artist1['ConstituentID'])
    ID_2 = int(artist2['ConstituentID'])
    return ID_1 < ID_2

def searchArtist (catalog,constituenID) : 
    """
    La funcion busca un artista por su constituent ID. 
    """
    artistas = catalog['artista']
    low = 0 
    high = lt.size(artistas)
    mid = 0 

    while low <= high : 
        mid = (high + low) // 2
        artist = lt.getElement(artistas,mid)
        ID = int(artist['ConstituentID'])
        if ID < constituenID : 
            low = mid + 1
        elif ID > constituenID : 
            high = mid - 1
        else : 
            return mid 

    return -1  
        


def rankArtbyCountry(catalog) : 
    """
    La funcion clasifica las obras por la nacionalidad de sus creadores 

    """
    ranking = {'NA' : lt.newList('ARRAY_LIST')}
    tamanio_artWork = lt.size(catalog['artWork'])
    sortArtists(catalog,2)
    i = 1 
    while i < tamanio_artWork :
        artWork = lt.getElement(catalog['artWork'],i)
        artWork['ArtistsNames'] = ""
        lista_ID = artWork['ConstituentID'].strip("[]").split(",") 
        for id in lista_ID :  
            ID = int(id)   
            pos_artist = searchArtist(catalog,ID)
            artistInfo = lt.getElement(catalog['artista'],pos_artist)
            artWork['ArtistsNames'] += artistInfo['DisplayName'] + ','
            procedencia = artistInfo['Nationality']
            if procedencia not in ranking.keys() and len(procedencia) > 0 : 
                ranking[procedencia] = lt.newList('ARRAY_LIST') 
                lt.addLast(ranking[procedencia],artWork)
            elif procedencia in ranking.keys() and len(procedencia) > 0: 
                lt.addLast(ranking[procedencia],artWork)
            else : 
                lt.addLast(ranking['NA'],artWork)
        i+=1 
    return ranking 

def sortRank (rank) : 
    """
    La funcion ordena la clasificacion de artWork por paises
    """
    lista = lt.newList('ARRAY_LIST')
    for k,v in rank.items() : 
        lt.addLast(lista,{"Nationality":k,"ArtWorks":v})
    lista_sort = ins.sort(lista,comp_tamanio)
    return lista_sort 

def comp_tamanio (elemento1,elemento2):
    t1 = lt.size(elemento1['ArtWorks'])
    t2 = lt.size(elemento2['ArtWorks'])
    return t1 < t2

#Funciones requerimiento 5. 
def clasificarporDepto (catalog,departamento) : 
    """
    Clasifica los artWorks por el departamento especificado. 
    """
    i = 1 
    artworks = lt.newList("ARRAY_LIST")
    while i <= lt.size(catalog['artWork']) : 
        artwork = lt.getElement(catalog['artWork'],i)
        if artwork['Department'] == departamento :
            lt.addLast(artworks,artwork)
    return artworks



def calcularCosto(artworks) : 
    i = 1 
    suma_costo = 0 
    peso_estimado = 0 
    while i <= lt.size(artworks) : 
        estimaciones = 0 
        artwork = lt.getElement(artworks['artWork'],i)
        peso = artwork['Weight']
        profundidad = artwork['Depth']
        alto = artwork['Height']
        ancho = artwork['Width']
        mas_costoso = 0 
        pesoKg = 0  
        costo_defecto = 48 
        costoArea = 0 
        costoVolumen = 0 
        costoKg = 0 

        if len(ancho) > 0 and len(alto) > 0 :
            anchoM = float(ancho)/100
            altoM = float(alto)/100
            Area = anchoM*altoM
            costoArea = 72*Area
            estimaciones += 1
            if len(profundidad) > 0 : 
                profundidadM = float(profundidad)/100
                Volumen = Area*profundidadM 
                costoVolumen = Volumen*72 
                estimaciones += 1
        if len(peso) > 0 : 
            pesoKg = float(peso) 
            costoKg = pesoKg*72
            estimaciones += 1 
        else :  
            costo_defecto = 48 
            mas_costoso = costo_defecto
        if estimaciones > 1 : 
            lista_costos = [costoKg,costoArea,costoVolumen]
            lista_ordenada = sorted(lista_costos,reverse=True)
            mas_costoso =  lista_ordenada[0]

        costoEstimado = mas_costoso + costoKg + costoArea + costoVolumen 
        suma_costo += costoEstimado
        artwork['Costo estimado'] = costoEstimado
        peso_estimado += pesoKg
        i += 1 
        return suma_costo, peso_estimado 
    
    def compareArtworkbyCost(artwork1,artwork2) : 
        costo1 = float(artwork1['Costo estimado']) 
        costo2 = float(artwork2['Costo estimado'])
        return costo1 < costo2
    
    def sortArtworksbyCost(artworks,orden) : 
        if orden == 1:
            ins.sort(artworks, compareArtworkbyCost)
        elif orden == 2:
            sa.sort(artworks, compareArtworkbyCost)
        elif orden == 3:
            mer.sort(artworks, compareArtworkbyCost)
        elif orden == 4:
            quic.sort(artworks, compareArtworkbyCost)

        


            


            

             
        

        
         
    
    


            
        
        

