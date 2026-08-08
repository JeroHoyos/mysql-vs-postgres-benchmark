import os
import time
import pandas as pd
from sqlalchemy import create_engine

BASE = os.path.dirname(os.path.abspath(__file__))

TABLES = ["especie", "entrenador", "tipo_de_objeto", "pokemon"]

DATABASES = ["pokemon_1k", "pokemon_10k", "pokemon_100k"]

CONNECTION = "postgresql+psycopg2://postgres:1234@localhost:5432/{database}"


def fetch_tables(url, tables=TABLES):
    with create_engine(url).connect() as connection:
        return {table: pd.read_sql(f"SELECT * FROM {table}", connection)
                for table in tables}


def query_1(url):
    tables = fetch_tables(url, ["pokemon", "especie", "entrenador"])
    with_species = tables["pokemon"].merge(tables["especie"],
                                           on="numero_de_pokedex")
    with_trainer = with_species.merge(tables["entrenador"],
                                      left_on="id_entrenador", right_on="id")
    fire_type = with_trainer[with_trainer["tipo_principal"] == "fuego"]
    return fire_type[["mote", "nombre_especie",
                      "puntos_de_velocidad", "nombre_completo"]]


def query_2(url):
    tables = fetch_tables(url, ["pokemon", "entrenador", "tipo_de_objeto"])
    with_trainer = tables["pokemon"].merge(tables["entrenador"],
                                           left_on="id_entrenador", right_on="id")
    with_item = with_trainer.merge(tables["tipo_de_objeto"],
                                   left_on="nombre_objeto", right_on="nombre")
    counts = with_item.groupby(["nombre_completo", "categoria"]).size()
    counts = counts.reset_index(name="total_pokemon")
    return counts.sort_values(["total_pokemon", "nombre_completo"],
                              ascending=[False, True])


def time_it(function, argument):
    start = time.perf_counter()
    result = function(argument)
    return result, (time.perf_counter() - start) * 1000


measurements = []

for database_name in DATABASES:
    url = CONNECTION.format(database=database_name)
    tables, fetch_time = time_it(fetch_tables, url)
    result_1, time_1 = time_it(query_1, url)
    result_2, time_2 = time_it(query_2, url)

    fetched_rows = sum(len(table) for table in tables.values())
    measurements.append([database_name, "fetch tables", fetch_time, fetched_rows])
    measurements.append([database_name, "query 1", time_1, len(result_1)])
    measurements.append([database_name, "query 2", time_2, len(result_2)])

    print(f"{database_name}: fetch {fetch_time:.3f} ms, "
          f"query 1 {time_1:.3f} ms, query 2 {time_2:.3f} ms")

times = pd.DataFrame(measurements, columns=["load", "step", "milliseconds", "rows"])
times.to_csv(os.path.join(BASE, "times.csv"), index=False)
print(times)
