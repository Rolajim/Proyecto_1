# MLops-Proyect  

### Sistema de recomendación

  
 <p align="center">  

<img src=https://www.enter.co/wp-content/uploads/2022/04/Plex-768x432.jpg> 

  
</p>





 ## Descripción de la problematica a resolver.  

  

Modelo de recomedación para usarios de plataformas de streaming. 

En este proyecto se desarrollará un modelo de recomendación de películas y series para una startup que provee servicios de agregación de plataformas de streaming.   

El objetivo es crear un interfase que ayude a los usuarios a descubrir nuevos contenidos que puedan interesarles.  

    
### Transformaciones de los datos solicitadas

Las transformacione se realizaron dentro de un notebook de colab llamado **"Mlops_ETL.ipynb"** donde se cargaron los dataset otorgados para el trabajo (4 de plataformas)(8 de ratings)

Para el desarrollo del MVP, se requiere rapidez y eficiencia en las transformaciones de los datos. Se realizarán las siguientes transformaciones:  

Generar un campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123).  

Reemplazar los valores nulos del campo rating por el string “G” (corresponde al maturity rating: “general for all audiences”).  

Dar formato AAAA-mm-dd a las fechas.  

Convertir los campos de texto a minúsculas.  

Convertir el campo duration en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).  

Luego de obtenido todos los cambios solicitados se crea un dataframe llamado "df_servicios_final.csv" sobre el cual trabajaremos el archivo que nos permitira generar las consultas de la Api

Desarrollo de la API  

Las funciones de consultas se encuentran en el archivo **"main.py"** el que fue relizado en visual studio code.

Se propone disponibilizar los datos de la empresa mediante una API desarrollada con el framework FastAPI. Las consultas que se pueden realizar son las siguientes:  

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type)).  

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year)).  

Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform)).  

Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year)).  

Antes de hacer el deploy en Deta una prueba en entorno virtual usando uvicorn para comprobar su funcionamiento.

### Deployment  

Se utilizó la plataforma Deta para realizar el deployment de la aplicación, ya que no requiere dockerización.
Análisis Exploratorio de los Datos (EDA)  

Una vez con los datos han sido limpiados, se realiza un análisis exploratorio de los mismos para investigar las relaciones entre las variables, detectar outliers o anomalías y encontrar patrones interesantes.Todo este proceso es realizado dentro de un notebok de colab llamado  **"MLops_EDA.ipynb"** que utiliza para tomar los datos el data set de nombre "df_unico.parquet", se utilizo la  librería dataprep  para realizar inside primario y obtener conclusiones relevantes, luego se generaron varios filtros dentro del daset para ver las tendecias de los usarios a mirar determinados contenidos.
Algunos datos relevantes:

Con 80.0% del porcentaje acumulado de usuarios, se tienen 30406 valores únicos que representan el 26.85% de todos los valores únicos de titulos disponibles.
La película mas vista "married at first sight", ha sido vista 302 veces.
la pelicula con mayor score "eddie izzard: force majeure:, con un score  3.81.
  

### Sistema de Recomendación  

Una vez que la API está lista y los datos han sido analizados se procede al entrenamiento del modelo de machine learning para crear un sistema de recomendación de películas y series. 

El notebook que contiene toda el códgo se llama **"MLops_Machine_Earning.ipynb"**, el modelo elegido para realizarlo es el SVD que pertenece a la libreria surprise 

Luego de creado se genera un arhivo ".sav"(el enlace al archivo se encuentra en los links debajo) para alojarlo en https://huggingface.co/, se creo un repositorio para hacer una interfaz para el usuario con la librería gradio.


El objetivo fue crear un sistema que dado un id de usuario y una película se la recomiende o no.  

 
 ## Links  

  ### Link del video explicativo del proceso de trabajo  

  `<link>` : <https://www.youtube.com/watch?v=TvUAlAHn26I>    

  ### Link a la api de consultas  

  `<link>` : <https://consultas-1-m0391132.deta.app/docs#/>
  
  ### Link al archivo que contiene el modelo entrenado
  
  `<link>` https://drive.google.com/file/d/1sXzl7sxAkaFxJzHJ7XY7TQniykS0lZDY/view?usp=share_link
  
  ### Link al sistema de recomendación  

 `<link>` : <https://huggingface.co/spaces/Rolajim/proyecto> 
