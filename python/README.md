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

Recorre los dos motores y las tres cargas, imprime los tiempos y los guarda
en `tiempos.csv`.

## Tiempos que mide

- `traer tablas` — lo que tarda en bajar las cuatro tablas a pandas
- `consulta 1` — el merge de las tres tablas y el filtro por tipo
- `consulta 2` — el merge, el group by y el orden

Para comparar con la fase III se usa el tiempo de las consultas. El de traer
las tablas va aparte porque en el SGBD ese paso no existe.
