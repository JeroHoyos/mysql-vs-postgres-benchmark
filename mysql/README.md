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
| Carga 1 | 1.000 | 457.290 ms |
| Carga 2 | 10.000 | 3955.518 ms |
| Carga 3 | 100.000 | 40036.582 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 1.140 ms | 8.942 ms | 88.969 ms |
| Consulta 2 | 7.494 ms | 77.024 ms | 902.467 ms |

## Fase IV: consultas en Python

| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 247.296 ms | 388.768 ms | 3703.509 ms |
| Consulta 1 | 25.575 ms | 10.136 ms | 100.473 ms |
| Consulta 2 | 13.681 ms | 22.631 ms | 239.285 ms |

| Consulta | Carga | MySQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 1.140 ms | 25.575 ms |
| Consulta 1 | 10k | 8.942 ms | 10.136 ms |
| Consulta 1 | 100k | 88.969 ms | 100.473 ms |
| Consulta 2 | 1k | 7.494 ms | 13.681 ms |
| Consulta 2 | 10k | 77.024 ms | 22.631 ms |
| Consulta 2 | 100k | 902.467 ms | 239.285 ms |
