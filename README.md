# Trabajo final BD1

Base de datos de pokémon en MySQL y PostgreSQL.

## Carpetas

- `mysql/` — esquema y consultas para MySQL
- `postgreSQL/` — esquema y consultas para PostgreSQL
- `carga_de_datos/` — datos de prueba (1k, 10k y 100k filas)
- `python/` — las mismas consultas resueltas con pandas

## Tablas

- `especie` — especies de pokémon y sus estadísticas
- `entrenador` — entrenadores
- `tipo_de_objeto` — objetos que puede llevar un pokémon
- `pokemon` — pokémon concretos de cada entrenador

## Uso

1. Crear las tablas con el `esquemas.txt` del motor que se use.
2. Cargar los datos de `carga_de_datos/` (se generan con `generar.py`, no están versionados).
3. Ejecutar las consultas de `consultas.txt` y medir los tiempos.
4. Ejecutar `python/consultas.py` para compararlos con pandas.
"# mysql-vs-postgres-benchmark" 
