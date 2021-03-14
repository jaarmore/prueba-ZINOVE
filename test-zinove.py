#!/usr/bin/env python
# coding: utf-8

# In[115]:


import hashlib
import pandas as pd
import requests
import sqlite3 as sql
import time


region_list = []
pais_region = []
idioma_pais = []
idioma_pais_sha1 = []
region_time = []
pais_languaje_time = []

# Defino el metodo obtener_regiones para conectarme a la API y obtener las regiones solicitadas
def obtener_regiones():
    
    # URL de la API
    url = "https://restcountries-v1.p.rapidapi.com/all"

    # Parametros de conexion a la API
    headers = {
        'x-rapidapi-key': "e7587a7eb9msh848cb75e1f97f04p12171ajsnfcd063290e3d",
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
        }
    
    # Consulto la API y convierto el resultado en formato JSON
    response = requests.request("GET", url, headers=headers)
    region_dict = response.json()
    
    # Dado que el resultado arroja regiones repetidas, defino un mecanismo para obtener solamente valores unicos
    for item in region_dict:
        if item['region'] not in region_list and item['region'] != '':
            t_inicio = time.time()
            region_list.append(item['region'])
            t_fin = time.time()
            region_time.append(t_fin - t_inicio)


obtener_regiones()
#print('regiones: {}'.format(region_list)) # imprimo todas las regiones obtenidas
#print('tiempos: {}'.format(region_time))

# Defino una funcion para obtener un pais por region
def obtener_pais_lenguaje(region):
    if region != '':
        url_pais = "https://restcountries.eu/rest/v2/region/{}".format(region)
        req = requests.get(url_pais)
        res_dict = req.json()[0]
        t_inicio = time.time()
        pais_region.append(res_dict['name'])
        idioma_pais.append(res_dict['languages'][0]['name'])
        t_fin = time.time()
        pais_languaje_time.append(t_fin - t_inicio)

# Mediante un loop recorro cada region obtenida para conectarme a siguiente API
# y obtener un pais por region y su respectivo lenguaje
for region in region_list:
    obtener_pais_lenguaje(region)

#print('Paises: {}'.format(pais_region))
#print('Paises - Lenguaje Time: {}'.format(pais_languaje_time))
#print(idioma_pais)

# De los idiomas obtenidos, defino la funcion para convertirlo a sha1
def convertir_idioma_sha1(languaje):
        result = hashlib.sha1(languaje.encode())
        idioma_pais_sha1.append(result.hexdigest().upper())

# Mediante un loop recorro cada idioma y lo envio a la funcion convertir_idioma_sha1, 
# para convertirlo a su respectivo algoritmo SHA1 y luego en letras mayusculas.
for languaje in idioma_pais:
    convertir_idioma_sha1(languaje)


#print('Lenguajes: {}'.format(idioma_pais_sha1))

# Calculo la columna de Time, con los datos obtenidos en las funciones anteriores.
def obtener_time():
    tot_time = []
    for index in range(0, len(region_list)):
        tot_time.append(region_time[index] + pais_languaje_time[index])
    return tot_time

pais_languaje_time = obtener_time()
#print('Tiempo: {}'.format(pais_languaje_time))

# Con los datos calculados, defino la funcion create_dataframe, con la cual
# creo la tabla con los datos solicitados, mediante un dataframe.
def create_dataframe():
    df = pd.DataFrame({
        "Region": region_list,
        "City_Name": pais_region,
        "Languaje": idioma_pais_sha1,
        "Time": pais_languaje_time
    })
    print(df)
    print()
    print('Total time: {}'.format(df['Time'].sum()))
    print('Average time: {}'.format(df['Time'].mean()))
    print('Min time: {}'.format(df['Time'].min()))
    print('Max time: {}'.format(df['Time'].max()))
    #print()
    #print(df.describe())
    return df

# Defino la funcion data_frame_to_sql para guardar los datos del dataframe
# en una base de datos sqlite3
def data_frame_to_sql(df):
    """
    Esta funcion recibe como argumento el dataframe creado en el metodo
    create_dataframe
    """
    conn = sql.connect('database.db') # Establezco la conexion a la base de datos 'database.db'
    df.to_sql('datos', conn, if_exists="replace") # Utilizo el metodo to_sql del dataframe para crear la tabla con los datos
    
    df1 = pd.read_sql('SELECT * FROM datos', conn)
    print()
    print('Data saved as SQL')
    print(df1)
    

# Defino la funcion data_frame_to_json, para almacenar el contenido del dataframe
# en un archivo JSON
def data_frame_to_json(df):
    """
    Esta funcion recibe como argumento el dataframe con los datos calculados
    en las funciones anteriores
    """
    df.to_json('file.json')
    print('DataFrame saved as json file')

df = create_dataframe()
data_frame_to_sql(df)
data_frame_to_json(df)

