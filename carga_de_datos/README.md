# Carga de datos

Datos de prueba en tres tamaños: `carga_1k/`, `carga_10k/` y `carga_100k/`.

Cada carpeta tiene un archivo por tabla con `INSERT` dentro de una transacción.
Sirven igual para MySQL y para PostgreSQL.

## Orden de carga

Por las claves foráneas hay que cargarlos así:

1. `especie.txt`
2. `entrenador.txt`
3. `tipo_de_objeto.txt`
4. `pokemon.txt`

## Regenerar

```
python generar.py
```

Usa una semilla fija, así que siempre salen los mismos datos.
