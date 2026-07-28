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
| Carga 1 | 1.000 | 107.232 ms |
| Carga 2 | 10.000 | 1030.287 ms |
| Carga 3 | 100.000 | 11282.137 ms |

## Fase III: consultas

| Consulta | 1k | 10k | 100k |
|---|---|---|---|
| Consulta 1 | 0.779 ms | 3.653 ms | 23.050 ms |
| Consulta 2 | 2.204 ms | 16.763 ms | 380.123 ms |

## Fase IV: consultas en Python


| Paso | 1k | 10k | 100k |
|---|---|---|---|
| Traer tablas | 155.098 ms | 93.729 ms | 834.794 ms |
| Consulta 1 | 3.694 ms | 6.304 ms | 45.886 ms |
| Consulta 2 | 3.593 ms | 13.325 ms | 149.844 ms |

| Consulta | Carga | PostgreSQL | Python |
|---|---|---|---|
| Consulta 1 | 1k | 0.779 ms | 3.694 ms |
| Consulta 1 | 10k | 3.653 ms | 6.304 ms |
| Consulta 1 | 100k | 23.050 ms | 45.886 ms |
| Consulta 2 | 1k | 2.204 ms | 3.593 ms |
| Consulta 2 | 10k | 16.763 ms | 13.325 ms |
| Consulta 2 | 100k | 380.123 ms | 149.844 ms |

