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


| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 102.735 ms | 157.031 ms | 1290.734 ms |
| Consulta 1 | 5.231 ms | 8.992 ms | 97.092 ms |
| Consulta 2 | 5.361 ms | 18.298 ms | 223.609 ms |

| Consulta | Carga | PostgreSQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 2.584 ms | 5.231 ms |
| Consulta 1 | 10k | 7.187 ms | 8.992 ms |
| Consulta 1 | 100k | 51.956 ms | 97.092 ms |
| Consulta 2 | 1k | 8.585 ms | 5.361 ms |
| Consulta 2 | 10k | 85.430 ms | 18.298 ms |
| Consulta 2 | 100k | 1128.943 ms | 223.609 ms |

