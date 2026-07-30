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
| Carga 1 | 1.000 | 226.006 ms |
| Carga 2 | 10.000 | 2252.994 ms |
| Carga 3 | 100.000 | 25784.750 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 2.928 ms | 6.994 ms | 52.796 ms |
| Consulta 2 | 8.393 ms | 82.338 ms | 1058.145 ms |

## Fase IV: consultas en Python


Cada medición arranca en la llamada a la base: abrir la conexión, traer las
tablas que la consulta necesita y resolverla con pandas.

| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 95.952 ms | 152.862 ms | 1222.129 ms |
| Consulta 1 | 30.413 ms | 125.677 ms | 1184.717 ms |
| Consulta 2 | 27.445 ms | 108.340 ms | 997.931 ms |

| Consulta | Carga | PostgreSQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 2.928 ms | 30.413 ms |
| Consulta 1 | 10k | 6.994 ms | 125.677 ms |
| Consulta 1 | 100k | 52.796 ms | 1184.717 ms |
| Consulta 2 | 1k | 8.393 ms | 27.445 ms |
| Consulta 2 | 10k | 82.338 ms | 108.340 ms |
| Consulta 2 | 100k | 1058.145 ms | 997.931 ms |

