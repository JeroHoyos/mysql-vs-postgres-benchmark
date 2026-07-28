import os
import time
import pandas as pd
from sqlalchemy import create_engine

BASE = os.path.dirname(os.path.abspath(__file__))

TABLAS = ["especie", "entrenador", "tipo_de_objeto", "pokemon"]

BASES_DE_DATOS = ["pokemon_1k", "pokemon_10k", "pokemon_100k"]

CONEXIONES = {
    "mysql": "mysql+pymysql://root:contrasena@localhost:3306/{base}",
    "postgresql": "postgresql+psycopg2://postgres:contrasena@localhost:5432/{base}",
}


def traer_tablas(url):
    with create_engine(url).connect() as conexion:
        return {tabla: pd.read_sql(f"SELECT * FROM {tabla}", conexion)
                for tabla in TABLAS}


def consulta_1(tablas):
    con_especie = tablas["pokemon"].merge(tablas["especie"],
                                          on="numero_de_pokedex")
    con_entrenador = con_especie.merge(tablas["entrenador"],
                                       left_on="id_entrenador", right_on="id")
    de_fuego = con_entrenador[con_entrenador["tipo_principal"] == "fuego"]
    return de_fuego[["mote", "nombre_especie",
                     "puntos_de_velocidad", "nombre_completo"]]


def consulta_2(tablas):
    con_entrenador = tablas["pokemon"].merge(tablas["entrenador"],
                                             left_on="id_entrenador", right_on="id")
    con_objeto = con_entrenador.merge(tablas["tipo_de_objeto"],
                                      left_on="nombre_objeto", right_on="nombre")
    conteo = con_objeto.groupby(["nombre_completo", "categoria"]).size()
    conteo = conteo.reset_index(name="total_pokemon")
    return conteo.sort_values(["total_pokemon", "nombre_completo"],
                              ascending=[False, True])


def cronometrar(funcion, argumento):
    inicio = time.perf_counter()
    resultado = funcion(argumento)
    return resultado, (time.perf_counter() - inicio) * 1000


medidas = []

for sgbd, plantilla in CONEXIONES.items():
    for nombre_base in BASES_DE_DATOS:
        url = plantilla.format(base=nombre_base)
        tablas, tiempo_traida = cronometrar(traer_tablas, url)
        resultado_1, tiempo_1 = cronometrar(consulta_1, tablas)
        resultado_2, tiempo_2 = cronometrar(consulta_2, tablas)

        filas_traidas = sum(len(tabla) for tabla in tablas.values())
        medidas.append([sgbd, nombre_base, "traer tablas", tiempo_traida, filas_traidas])
        medidas.append([sgbd, nombre_base, "consulta 1", tiempo_1, len(resultado_1)])
        medidas.append([sgbd, nombre_base, "consulta 2", tiempo_2, len(resultado_2)])

        print(f"{sgbd} {nombre_base}: traer {tiempo_traida:.3f} ms, "
              f"consulta 1 {tiempo_1:.3f} ms, consulta 2 {tiempo_2:.3f} ms")

tiempos = pd.DataFrame(medidas, columns=["sgbd", "carga", "paso", "milisegundos", "filas"])
tiempos.to_csv(os.path.join(BASE, "tiempos.csv"), index=False)
print(tiempos)
