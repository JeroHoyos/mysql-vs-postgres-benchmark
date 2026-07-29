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
| Carga 1 | 1.000 | 245.210 ms |
| Carga 2 | 10.000 | 2457.478 ms |
| Carga 3 | 100.000 | 27478.432 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 3.202 ms | 7.374 ms | 54.962 ms |
| Consulta 2 | 10.041 ms | 88.871 ms | 1161.557 ms |

## Fase IV: consultas en Python


Cada medición arranca en la llamada a la base: abrir la conexión, traer las
tablas que la consulta necesita y resolverla con pandas.

| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 169.216 ms | 159.809 ms | 1294.557 ms |
| Consulta 1 | 44.244 ms | 134.529 ms | 1265.147 ms |
| Consulta 2 | 33.723 ms | 117.859 ms | 1066.019 ms |

| Consulta | Carga | PostgreSQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 3.202 ms | 44.244 ms |
| Consulta 1 | 10k | 7.374 ms | 134.529 ms |
| Consulta 1 | 100k | 54.962 ms | 1265.147 ms |
| Consulta 2 | 1k | 10.041 ms | 33.723 ms |
| Consulta 2 | 10k | 88.871 ms | 117.859 ms |
| Consulta 2 | 100k | 1161.557 ms | 1066.019 ms |

