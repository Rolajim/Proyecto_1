from fastapi import FastAPI
import pandas as pd
import numpy as np
from typing import List

app= FastAPI()

    # Primera función solcicitada get_max_duration
    # 1 Generamos los diccionarios de combinaciones de letras para cada opción
    # 2 Buscamos la plataforma correspondiente en el diccionario
    # 3 Buscamos el tipo de duración correspondiente en el diccionario
    # 4 Cargamos de archivo CSV en un DataFrame de Pandas
    # 5 Filtramos el DataFrame
    # 6 Ordenamos el DataFrame y obtener la fila con la duración máxima
df = pd.read_csv('df_servicios_final.csv')

@app.get("/get_max_duration")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # 1
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    duration_dict = {'min': ['min', 'mi', 'm'], 'season': ['season', 's', 'se', 'sea', 'seas', 'seaso']}

    # 2
    platform_full = platform_dict.get(platform, platform)

    # 3
    duration_type_full = duration_type
    for duration, combos in duration_dict.items():
        if duration_type in combos:
            duration_type_full = duration

    # 4
    global df

    # 5
    if duration_type_full is not None:
        filtered_df = df[df['duration_type'] == duration_type_full]
    else:
        filtered_df = df.copy()
    if year is not None:
        filtered_df = filtered_df[filtered_df['year'] == year]
    if platform_full is not None:
        filtered_df = filtered_df[filtered_df['platform'] == platform_full]

    # 6
    sorted_df = filtered_df.sort_values(by='duration_int', ascending=False)
    max_duration = sorted_df.iloc[0][['title']]

    return max_duration

    # Segunda función solcicitada get_score_count
    # 1 Generaramos el diccionario de combinaciones de letras para cada plataforma
    # 2 Buscamos la plataforma correspondiente en el diccionario
    # 3 Cargamos el archivo CSV en un DataFrame de Pandas
    # 4 Contamos el número de veces que se cumple la condición
    # 5 Devolvemos la cantidad de veces que se cumple la condición

@app.get("/get_score_count/{platform}/{Scored}/{year}")
def get_score_count(platform: str, Scored: int, year: int):
    # 1
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                            'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                            'hulu': ['h', 'hu', 'hul', 'hulu'],
                            'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # 2
    platform_full = platform_dict.get(platform, platform)

    # 3
    global df

    # 4
    cantidad = np.count_nonzero(np.where((df["platform"] == platform_full) & (df["Scored"] >=Scored) & (df["year"] == year), True, False))

    # 5
    return cantidad

    # Tercera función solicitada get_count_platform
    # 1 Generamos el diccionario de combinaciones de letras para cada plataforma
    # 2 Buscamos la plataforma correspondiente en el diccionario
    # 3 Cargamos el archivo CSV en un DataFrame de Pandas
    # 4 Contamos el número de veces que se cumple la condición
    # 5 Devolvemos la cantidad de veces que se cumple la condición

@app.get("/get_count_platform/{platform}")
def get_count_platform(platform: str):
    # 1
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # 2
    platform_full = platform_dict.get(platform, platform)

    # 3
    global df

    # 4
    cantidad = np.count_nonzero((df["platform"] == platform_full))

    # 5
    return cantidad



    # Cuarta función solicitada get_actor
    # 1 Generamos el diccionario de combinaciones de letras para cada plataforma
    # 2 Buscamos la plataforma correspondiente en el diccionario
    # 3 Cargamos el archivo CSV en un DataFrame de Pandas
    # 4 Filtramos por año y plataforma
    # 5 Contamos la cantidad de veces que aparece cada actor en la columna 'cast'
    # 6 Devolvemos la cantiad de veces que se repite el actor


@app.get("/get_actor/{platform}/{release_year}")
def get_actor(platform: str, release_year: int):
    # 1
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # 2
    platform_full = platform_dict.get(platform, platform)

    # 3
    global df

    # 4
    filtered_df = df[(df['platform'] == platform_full) & (df['year'] == release_year)]

    # 5
    actor_count = filtered_df['cast'].str.split(',').explode().str.strip().value_counts()

    # 6
    if actor_count.empty:
        return None
    else:
        return actor_count.index[0]
