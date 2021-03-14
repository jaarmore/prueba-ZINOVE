# Prueba tecnica ZINOVE

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1.
3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json
9. La prueba debe ser entregada en un repositorio git.


**Es un plus si:**
* No usa famework
* Entrega Test Unitarios
* Presenta un diseño de su solucion.


## Solucion propuesta
+ Consumir API para obtener regiones (Utilizare la libreria request para obtener los datos) y posteriormente, crear un listado de las diferentes regiones.
+ En base al listado anterior consumir la API https://restcountries.eu/, y obtener un pais por cada region, de la misma forma utilizare la libreria requests para conseguir tal proposito. En este punto hare una sola consulta utilizando la lista de regiones para obtener tanto el pais como el idioma que se habla en el mismo.
+ Para calcular el tiempo que me toma armar cada fila, utilizare la libreria time de python, la cual me permitira establecer un tiempo inicial al momento de empezar con la busqueda de los datos y un tiempo final una vez terminado el proceso, la resta entre tiempo final y tiempo inicial me dara el valor para cada campo, luego hare una suma de los diferentes tiempos obtenidos por cada campo y con estos tendre el tiempo total de armado de cada registro en la tabla.
+ En la creacion de la tabla, utilizare un DataFrame de la libreria Pandas en Python.
+ Utilizare la libreria sqlite3 nativa en python, para mediante los metodos del DataFrame, hacer el volcado de la tabla a una base de datos SQL.
+ De la misma forma que el paso anterior, utilizare el metodo to_json del dataFrame para crear un archivo .JSON con los datos de la tabla.

La solucion propuesta se encuentra detallada en el libro: [Solucion](https://github.com/jaarmore/prueba-ZINOVE/blob/main/test-zinove.ipynb)

El archivo python, con el codigo fuente esta en [Fuente](https://github.com/jaarmore/prueba-ZINOVE/blob/main/test-zinove.py)

Los archivos `database.db` y `file.json` son generados durante la ejecucion del programa.

### AUTHOR
**Jackson Moreno**

