<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Willi Cutzal`**</h1>

# <h1 align=center>**`Data Engineer`**</h1>


¡Bienvenido a mi primer proyecto individual de la etapa de labs! En esta ocasión me situo en el rol de un ***Data Engineer***.  

<hr>  

## **Introducción**
El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente realizar el proceso de **ETL** y aplicar las transformaciones pertinentes. Luego disponibilizar los datos limpios para su consulta a través de una API, la misma será construida con **FastAPI** un web framework de alto rendimiento. Y finalmente, la API será empaquetada en un entorno virtual dockerizado.

¿Qué es una API?

`Application Programming Interface` es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>




Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

## **Pasos del proyecto**

1. Analisis exploratorio de datos. Normalización de datos. Básicamente el proceso de ETL se llevará a cabo con la librería **Pandas** de Python

2. Trabajar las consultas, por medio de un jupyter notebook.

3. Creación de la API con FastAPI, esta estará en nuestro archivo **main.py**

4. Empaquetar la aplicación en un contenedor de Docker

<p align=center>
<img src = 'https://i.postimg.cc/2SwvnTcw/Sin-t-tulo.png' height = 300></p>


## **Conceptos de interés**

- **`Docker`** es una solución completa para la producción, distribución y uso de containers.  
&nbsp;- **`Container`** es una abstracción de la capa de software que permite *empaquetar* código, con librerías y dependencias en un entorno parcialmente aislado.  
&nbsp;- **`Image`** es un ejecutable Docker que tiene todo lo necesario para correr aplicaciones, lo que incluye un archivo de configuración, variables -de entorno y runtime- y librerías.  
&nbsp;- **`Dockerfile`** archivo de texto con instrucciones para construir una imagen. Puede considerarse la automatización de creación de imágenes.

## **Recursos y links provistos**

Imagen Docker con Uvicorn/Guinicorn para aplicaciones web de alta performance:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker


FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/

