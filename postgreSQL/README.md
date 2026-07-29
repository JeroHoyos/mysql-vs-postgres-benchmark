# PostgreSQL

- `esquemas.txt` — las cuatro tablas.
- `consultas/consulta_1.sql` — pokémon de tipo fuego con su especie y su entrenador.
- `consultas/consulta_2.sql` — pokémon de cada entrenador por categoría de objeto.
- `carga_de_datos/carga_{1k,10k,100k}.sql` — una prueba de carga cada uno.
- `python/consultas.py` — las mismas consultas resueltas con pandas.

Cada archivo de carga crea las tablas y las carga, así que no hace falta correr
`esquemas.txt` antes.

## Fase II: carga

| Prueba | Filas por tabla | Tiempo |
|---|---|---|
| Carga 1 | 1.000 | 239.662 ms |
| Carga 2 | 10.000 | 2527.523 ms |
| Carga 3 | 100.000 | 29055.644 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 2.584 ms | 7.187 ms | 51.956 ms |
| Consulta 2 | 8.585 ms | 85.430 ms | 1128.943 ms |

## Fase IV: consultas en Python


Cada medición arranca en la llamada a la base: abrir la conexión, traer las
tablas que la consulta necesita y resolverla con pandas.

| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 79.344 ms | 96.608 ms | 762.568 ms |
| Consulta 1 | 44.226 ms | 121.534 ms | 777.474 ms |
| Consulta 2 | 44.908 ms | 87.011 ms | 868.397 ms |

| Consulta | Carga | PostgreSQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 2.584 ms | 44.226 ms |
| Consulta 1 | 10k | 7.187 ms | 121.534 ms |
| Consulta 1 | 100k | 51.956 ms | 777.474 ms |
| Consulta 2 | 1k | 8.585 ms | 44.908 ms |
| Consulta 2 | 10k | 85.430 ms | 87.011 ms |
| Consulta 2 | 100k | 1128.943 ms | 868.397 ms |

