# MLops-Proyect  

### Sistema de recomendación

  
 <p align="center">  

<img src=https://www.enter.co/wp-content/uploads/2022/04/Plex-768x432.jpg> 

  
</p>  

  

    

  ## Descripción de la problematica a resolver.  

  

Modelo de Recomendación para Servicios de Agregación de Plataformas de Streaming  

En este proyecto se desarrollará un modelo de recomendación de películas y series para una startup que provee servicios de agregación de plataformas de streaming.   

El objetivo es crear un sistema de recomendación que ayude a los usuarios a descubrir nuevos contenidos que puedan interesarles.  

Contexto    

El modelo de recomendación ya ha sido entrenado y ha arrojado buenas métricas, pero ahora es necesario llevarlo al mundo real. El ciclo de vida de un proyecto de Machine Learning debe contemplar desde la recolección y tratamiento de los datos hasta el entrenamiento y mantenimiento del modelo. En este caso, el rol a desarrollar es el de Data Scientist, encargado de transformar los datos y desarrollar una API que permita consultarlos.  

Propuesta de Trabajo  

Transformaciones de los Datos  

Para el desarrollo del MVP, se requiere rapidez y eficiencia en las transformaciones de los datos. Se realizarán las siguientes transformaciones:  

Generar un campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123).  

Reemplazar los valores nulos del campo rating por el string “G” (corresponde al maturity rating: “general for all audiences”).  

Dar formato AAAA-mm-dd a las fechas.  

Convertir los campos de texto a minúsculas.  

Convertir el campo duration en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).  

Desarrollo de la API  

Se propone disponibilizar los datos de la empresa mediante una API desarrollada con el framework FastAPI. Las consultas que se pueden realizar son las siguientes:  

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type)).  

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year)).  

Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform)).  

Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year)).  

Deployment  

Se utilizará la plataforma Deta para realizar el deployment de la aplicación, ya que no requiere dockerización y ha sido utilizado con éxito por los compañeros cercanos.    

Análisis Exploratorio de los Datos (EDA)  

Una vez que los datos han sido limpiados, se realizará un análisis exploratorio de los mismos para investigar las relaciones entre las variables, detectar outliers o anomalías y encontrar patrones interesantes. Se utilizo la librería dataprep  para realizar el análisis y obtener conclusiones relevantes, luego se generaron varios filtros dentro del daset para ver las tendecias de los usarios a mirar determinados contenidos   
  

Sistema de Recomendación  

Una vez que la API está lista y los datos han sido analizados el quido de data procederá al entrenamiento del modelo de machine learning para crear un sistema de recomendación de películas y series.   

El objetivo fue crear un sistema que dado un id de usuario y una película se la recomiende o no.  

 
 ###Links  

  #Link del video explicativo del proceso de trabajo  

  `<link>` : <https://www.youtube.com/watch?v=TvUAlAHn26I>    

  #Link a la api de consultas  

  `<link>` : <https://consultas-1-m0391132.deta.app/docs#/>  

  #Link al sistema de recomendación  

 `<link>` : <https://huggingface.co/spaces/Rolajim/proyecto> 

