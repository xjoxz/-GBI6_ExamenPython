def download_pubmed(keyword):
    """
    Muestras de IDs de la busqueda en pubmed
    """
    from Bio import Entrez
    from Bio import SeqIO
    from Bio import GenBank 
    Entrez.email = 'josue.chango@est.ikiam.edu.ec'
    handle = Entrez.esearch(db='pubmed',
                        sort='relevance',
                        retmax='200',
                        retmode='xml',
                        term=keyword)
    results = Entrez.read(handle)
    id_list = results["IdList"]
    ids = ','.join(id_list)
    Entrez.email = 'josue.chango@est.ikiam.edu.ec'
    handle = Entrez.efetch(db='pubmed',
                       retmode='xml',
                       id=ids)
    lista_id = ids.split(",")
    return (lista_id) 


import csv 
import re
import pandas as pd 
from collections import Counter

def map_science(tipo):
    """ Docstring map_science """
    """ Esta funcion me permite crear un MapOfScience """
    #if tipo == "AD":
    with open() as f:
        my_text = f.read(tipo)
    my_text = re.sub(r'\n\s{6}', ' ', my_text)  
    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
    unique_zipcodes = list(set(zipcodes))
    unique_zipcodes.sort()
    unique_zipcodes[:10]
    zip_coordinates = {}
    with open('CSB-master/regex/data/MapOfScience/zipcodes_coordinates.txt') as f:
        csvr = csv.DictReader(f)
        for row in csvr:
         zip_coordinates[row['ZIP']] = [float(row['LAT']), 
                                        float(row['LNG'])]
    zip_code = []
    zip_long = []
    zip_lat = []
    zip_count = []
    for z in unique_zipcodes:
    # if we can find the coordinates
        if z in zip_coordinates.keys():
            zip_code.append(z)
            zip_lat.append(zip_coordinates[z][0])
            zip_long.append(zip_coordinates[z][1])
            zip_count.append(zipcodes.count(z))
    import matplotlib.pyplot as plt
    #%matplotlib inline
    plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
    plt.colorbar()
# only continental us without Alaska
    plt.xlim(-125,-65)
    plt.ylim(23, 50)
# add a few cities for reference (optional)
    ard = dict(arrowstyle="->")
    plt.annotate('Filadelfia', xy = (-122.1381, 37.4292), 
                   xytext = (-112.1381, 37.4292), arrowprops= ard)
    plt.annotate('San Francisco', xy = (-71.1106, 42.3736), 
                   xytext = (-73.1106, 48.3736), arrowprops= ard)
    plt.annotate('Atlanta', xy = (-87.6847, 41.8369), 
                   xytext = (-87.6847, 46.8369), arrowprops= ard)
    plt.annotate('Detroit', xy = (-122.33, 47.61), 
                   xytext = (-116.33, 47.61), arrowprops= ard)
    plt.annotate('Dallas', xy = (-80.21, 25.7753), 
                   xytext = (-80.21, 30.7753), arrowprops= ard)
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    return

import miningscience as msc 
help(download_pubmed)
help(map_science)