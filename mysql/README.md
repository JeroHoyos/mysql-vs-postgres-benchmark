# MySQL

`esquemas.txt` crea las cuatro tablas.

```
mysql -u usuario -p base_de_datos < esquemas.txt
```

Usa `AUTO_INCREMENT` para las claves y `DECIMAL(10,2)` para el dinero.

Las dos consultas de la fase III están en `consultas/`, una por archivo. Cada una
mide su propio tiempo y lo devuelve como `tiempo_de_la_consulta`.

- `consultas/consulta_1.sql` — pokémon de tipo fuego con su especie y su entrenador.
- `consultas/consulta_2.sql` — pokémon de cada entrenador por categoría de objeto.
