\timing on

SELECT entrenador.nombre_completo,
       tipo_de_objeto.categoria,
       COUNT(*) AS total_pokemon
FROM pokemon
JOIN entrenador ON pokemon.id_entrenador = entrenador.id
JOIN tipo_de_objeto ON pokemon.nombre_objeto = tipo_de_objeto.nombre
GROUP BY entrenador.nombre_completo, tipo_de_objeto.categoria
ORDER BY total_pokemon DESC, entrenador.nombre_completo;
