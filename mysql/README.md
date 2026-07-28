# MySQL

`esquemas.txt` crea las cuatro tablas.

```
mysql -u usuario -p base_de_datos < esquemas.txt
```

Usa `AUTO_INCREMENT` para las claves y `DECIMAL(10,2)` para el dinero.

`consultas.txt` tiene las dos consultas de la fase III. Para medir el tiempo:

```
SET profiling = 1;
-- ejecutar las consultas
SHOW PROFILES;
```
