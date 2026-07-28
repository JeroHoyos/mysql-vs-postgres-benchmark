# PostgreSQL

`esquemas.txt` crea las cuatro tablas.

```
psql -U usuario -d base_de_datos -f esquemas.txt
```

Usa `SERIAL` para las claves y `NUMERIC(10,2)` para el dinero.

`consultas.txt` tiene las dos consultas de la fase III. Para medir el tiempo,
en psql: `\timing on`
