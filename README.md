# <div align='center' >PROYECTO INDIVIDUAL N° 2: DATA ANALYTICS
<div style="height:50vh;" align='center'><img src="https://th.bing.com/th/id/R.c3e9601a3f07e5c22426b0be07e83dfe?rik=ShCKTkHy0rablw&riu=http%3a%2f%2ftechblogcorner.com%2fwp-content%2fuploads%2f2018%2f07%2fOnline_video_analytics_tools_original.jpg&ehk=6LNbFWb2Swutd6NAcs7FGMeqG%2b%2fWhjqDksGoyj%2fY1F4%3d&risl=&pid=ImgRaw&r=0"></div>
</div>

## Tabla de contenido
1. [Herramientas y Librerias Utilizadas](#herramientas-y-librerias-utilizadas)
2. [Estuctura del Proyecto](#estructura-del-proyecto)
3. [Contexto](#contexto)
4. [Previsualizacion](#previsualizacion)
6. [Metodologia](#metodologia)
7. [Conclusiones](#conclusiones)
8. [Datasets](#datasets)
9. [Autor](#autor) 

## Herramientas y Librerias Utilizadas
Para el siguiente proyecto se hizo uso de las siguientes herramientas y librerias (el conocimiento sobre los mismos no require de un nivel avanzado para el entendimiento del proyecto):
1. ***Python***
2. ***Jupyter Notebook***
3. ***Pandas***
4. ***PowerBI***
4. ***MySQL***
5. ***Web Scrapping*** **(librerias: requests y bs4)**
6. ***MatplotLib***
7. ***Seaborn***
8. ***pymysql***
9. ***sqlalchemy***

## Estructura del proyecto
`/dashboard`: Carpeta que contiene el dashboard interactivo para presentar tendencias y patrones. <br>
`/datasets`: Carpeta que contiene los datasets utilizados en el proyecto. <br>
`/notebooks`: Carpeta que contiene el archivo `eda.ipynb` donde se analizaron y limpiaron los datasets. Este es el unico archivo del proyecto que necesitaras correr. A su vez, esta capeta contiene el archivo que realiza un scrapping (`scrap_dolar.py`) para accedar al precio del dolar oficial en Argentina.<br>
`img`: Imagenes utilizadas en el proyecto.

## Contexto
En el presente proyecto se aborda la problematica de una empresa de telecomunicaciones (especificamente, haremos referencia a proveedores de internet), en conocer como se va desarrollando y evolucionando con el pasar de los años. Para lograr esto se realiza una busqueda de tendencias y patrones que puedan dirigir hipotesis y conclusiones para un mejor desempeño en el futuro. Ya con esto en mente, en los siguientes apartado se detallará los pasos y conclusiones que fueron surgiendo durante este proyecto. La fuente de datos original se encuentra citada en el apartado [Datasets](#datasets) o bien puedes hacer uso de la carpeta `/datasets` si asi lo prefieres.

## Previsualizacion
Antes de comenzar de lleno con el analisis de los datos, lo primero que se realizo, fue una previsualizacion del dataset `internet`, el cual contaba con una cantidad considerable de tablas u <i>hojas</i> (ya que el mismo se encuentra en formato de archivo de excel). Primeras observaciones:

1. Las <i>hojas</i> `Acc_vel_loc_sinrangos` y `Velocidad_sin_Rangos` fueron descartadas para este analisis ya que cuenta con gran cantidad de valores nulos, si bien estos podrian ser rellenados (utilizando la media,moda o mediana), podriamos generar una ponderacion imprecisa, dificultando un posterior analisis e/o hipotesis. Ademas, basandonos en los nombres de las columnas, podemos ver que no presentan valores muy distante entre si. Ejemplo: columna <b>2 Mbps</b> y columna <b>2.2 Mbps</b>.
2. La <i>hoja</i> `Accesos_tecnologia_localidad` tambien fue descartada por uno de los motivos descriptos en el punto anterior, presenta gran cantidad de nulos, dificultando el futuro analisis.
3. Las <i>hojas</i> no mencionadas son con las que se trabajará, ya que sugieren tener mayor calidad en los datos y podrian aportar mayor informacion al analisis.

## Metodologia
Una vez que seleccionamos los archivos a trabajar, se procedio a realizar un Analisis Exploratorio de los Datos (puedes verlo haciendo click [aqui](./notebooks/eda.ipynb) o dirigendote a `/notebooks/eda.ipynb`). Acompañamos este analisis utilizando librerias de manejo de dataframes y limpieza de datos como `pandas`. Tambien se grafico el comportamiento de datos con las librerias `matplotlib` y `seaborn`, para luego, una vez finalizado el analisis y la limpieza, llevar los datos a <b>MySQL</b>. Ya con los datos alli, la base de datos se conectó con `PowerBI`, donde se procedio a realizar el dashboard.

## Conclusiones
### <p align='center'><b>Tecnologias</b><p>
Una vez finalizado el dashboard, lo primero que se llega a concluir es que las tecnologias `Dial-up` y `ADSL` decrecen año tras año en la cantidad de gente que tiene acceso a estos servicios, pudiendo significar en un futuro, un posible corte en el mantenimiento de estos. Esto es perfectamente observable en los graficos, donde del año 2014 al año 2023, disminuyeron en un 50% la cantidad de accesos a tales tecnologias. 
Por contraparte, la tecnologia `Fibra Optica` y `Wireless`, parecen estar cada año más en auge, incrementando considerablemente. Debido a esto, se les hizo énfasis en el `dashboard`, y se planteó como objetivo aumentar el acceso a tales servicios trimestralmente.
Por ultimo pero no menos importante, comentar que, si bien la tecnologia `Cable Modem` sigue siendo la que lidera las estadistica, desde el año 2020 que no ha tenido una suba importante. En un futuro cercano, observando las tendencias y los patrones, la `Fibra Optica` podria liderar el mercado.

### <p align='center'><b>Velocidad y Accesos por provincia</b><p>
Al igual que en el apartado anterior, es notable el aumento anual de la ***velocidad media de bajada*** y de los ***accesos a las tecnologias*** sin importar de que provincia estemos hablando. Sin embargo, cabe recalcar que Capital Federal es la que generalmente lidera las estadisticas. 
Dentro de las tendencias y patrones encontrados, se destaca un punto de inflexion entre el año 2017 y 2018, a partir de los cuales el incremento tanto en la velocidad como en el acceso a tecnologias, es destacable. Si bien no hay valores que podamos catalogar como valores disruptivos, si hay algunos datos que estan considerablemente alejados de la media.Tal es el caso de la provincia de San Luis. Si nos situamos en el año 2018, podremos observar un gran aumento en la cantidad de hogares que tienen acceso a internet durante este año. Tambien remarcar el caso de Catamarca para el año 2019 con respecto al gran aumento de accesos a **fibra optica** en ese año .Te invito a que habras el archivo `/dashboard/dashboard_internet.pbix` para que lo veas por tu propia cuenta.

### <p align='center'><b>Ingresos</b><p>
Cuando se realizo el analisis al archivo `ingresos`, fue destacable un aumento continuo durante todos los años, pudiendo significar que la actividad economica venia al alza. Sin embargo, cuando transformabamos esto datos a valores basados en el dolar estadounidense, presentó altibajos.
Al igual que lo comentado en el tópico anterior, se distingue el año 2017. En este periodo, los ingresos (en dolares) fueron notablemente superior al resto de los años. 

## Datasets
Los datos utilizados provienen del libro de excel `internet` que provee el Ente Nacional de Comunicaciones argentino <b>(ENACOM)</b>, contenido en el siguiente <a href="https://indicadores.enacom.gob.ar/datos-abiertos">enlace</a>.

## Autor
Este proyecto fue realizado por Martin Ferrari. Muchas gracias a todos por leer, no dudes en contactarme a mi <a href="https://www.linkedin.com/in/martin-ferrari-bb0547219/">LinkedIn</a> por cualquier duda.

