# Fase IV: consultas en Python

`consultas.py` trae las tablas con `SELECT * FROM tabla`, las guarda en
DataFrames de pandas y resuelve ahí las dos consultas de la fase III.

## Instalar

```
pip install -r requirements.txt
```

## Configurar

Al principio de `consultas.py` están el usuario, la contraseña y los nombres
de las bases (`pokemon_1k`, `pokemon_10k`, `pokemon_100k`). Hay que cambiarlos
por los propios.

## Ejecutar

```
python consultas.py
```

Recorre los dos motores y las tres cargas, imprime los tiempos en ms y los
guarda en `tiempos.csv`.

## Tiempos en Python

`traer tablas` es lo que tarda en bajar las cuatro tablas a pandas. Va aparte
porque en el SGBD ese paso no existe.

| Motor | Carga | Traer tablas | Consulta 1 | Consulta 2 |
|---|---|---|---|---|
| MySQL | 1k | | | |
| MySQL | 10k | | | |
| MySQL | 100k | | | |
| PostgreSQL | 1k | | | |
| PostgreSQL | 10k | | | |
| PostgreSQL | 100k | | | |

## Python contra el SGBD

Los tiempos del SGBD salen de las tablas de la fase III en `postgreSQL/README.md`
y `mysql/README.md`.

| Motor | Consulta | Carga | SGBD (fase III) | Python (fase IV) |
|---|---|---|---|---|
| MySQL | Consulta 1 | 1k | | |
| MySQL | Consulta 1 | 10k | | |
| MySQL | Consulta 1 | 100k | | |
| MySQL | Consulta 2 | 1k | | |
| MySQL | Consulta 2 | 10k | | |
| MySQL | Consulta 2 | 100k | | |
| PostgreSQL | Consulta 1 | 1k | | |
| PostgreSQL | Consulta 1 | 10k | | |
| PostgreSQL | Consulta 1 | 100k | | |
| PostgreSQL | Consulta 2 | 1k | | |
| PostgreSQL | Consulta 2 | 10k | | |
| PostgreSQL | Consulta 2 | 100k | | |
