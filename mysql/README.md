# MySQL

- `esquemas.txt` — las cuatro tablas.
- `consultas/consulta_1.sql` — pokémon de tipo fuego con su especie y su entrenador.
- `consultas/consulta_2.sql` — pokémon de cada entrenador por categoría de objeto.
- `carga_de_datos/carga_{1k,10k,100k}.sql` — una prueba de carga cada uno.
- `python/consultas.py` — las mismas consultas resueltas con pandas.

Cada archivo de carga crea las tablas y las carga, así que no hace falta correr
`esquemas.txt` antes.

Cada carga se hizo sobre su propia base de datos (`pokemon_1k`, `pokemon_10k`,
`pokemon_100k`), igual que en PostgreSQL.

## Fase II: carga

| Prueba | Filas por tabla | Tiempo |
|---|---|---|
| Carga 1 | 1.000 | 404.248 ms |
| Carga 2 | 10.000 | 3913.301 ms |
| Carga 3 | 100.000 | 38896.834 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 1.248 ms | 10.371 ms | 90.512 ms |
| Consulta 2 | 7.149 ms | 78.263 ms | 901.164 ms |

## Fase IV: consultas en Python

Cada medición arranca en la llamada a la base: abrir la conexión, traer las
tablas que la consulta necesita y resolverla con pandas.

| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 124.687 ms | 398.721 ms | 3871.870 ms |
| Consulta 1 | 60.530 ms | 355.877 ms | 3396.875 ms |
| Consulta 2 | 49.629 ms | 273.342 ms | 2749.970 ms |

| Consulta | Carga | MySQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 1.248 ms | 60.530 ms |
| Consulta 1 | 10k | 10.371 ms | 355.877 ms |
| Consulta 1 | 100k | 90.512 ms | 3396.875 ms |
| Consulta 2 | 1k | 7.149 ms | 49.629 ms |
| Consulta 2 | 10k | 78.263 ms | 273.342 ms |
| Consulta 2 | 100k | 901.164 ms | 2749.970 ms |
