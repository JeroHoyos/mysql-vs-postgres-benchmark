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
| Carga 1 | 1.000 | 370.492 ms |
| Carga 2 | 10.000 | 3596.290 ms |
| Carga 3 | 100.000 | 35933.864 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 1.120 ms | 12.144 ms | 119.870 ms |
| Consulta 2 | 7.281 ms | 100.983 ms | 1043.776 ms |

## Fase IV: consultas en Python

Cada medición arranca en la llamada a la base: abrir la conexión, traer las
tablas que la consulta necesita y resolverla con pandas.

| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 82.083 ms | 364.944 ms | 3595.773 ms |
| Consulta 1 | 48.183 ms | 323.382 ms | 3064.940 ms |
| Consulta 2 | 40.885 ms | 247.794 ms | 2543.436 ms |

| Consulta | Carga | MySQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 1.120 ms | 48.183 ms |
| Consulta 1 | 10k | 12.144 ms | 323.382 ms |
| Consulta 1 | 100k | 119.870 ms | 3064.940 ms |
| Consulta 2 | 1k | 7.281 ms | 40.885 ms |
| Consulta 2 | 10k | 100.983 ms | 247.794 ms |
| Consulta 2 | 100k | 1043.776 ms | 2543.436 ms |
