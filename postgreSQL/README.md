# PostgreSQL

- `esquemas.txt` — las cuatro tablas.
- `consultas/consulta_1.sql` — pokémon de tipo fuego con su especie y su entrenador.
- `consultas/consulta_2.sql` — pokémon de cada entrenador por categoría de objeto.
- `carga_de_datos/carga_{1k,10k,100k}.sql` — una prueba de carga cada uno.

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
| Consulta 1 | 0,779 ms | 3.653 ms | 23.050 ms |
| Consulta 2 | 2.204 ms | 16.763 ms | 380.123 ms |
