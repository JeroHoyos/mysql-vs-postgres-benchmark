SET @inicio = NOW(6);

SELECT pokemon.mote,
       especie.nombre_especie,
       especie.puntos_de_velocidad,
       entrenador.nombre_completo
FROM pokemon
JOIN especie ON pokemon.numero_de_pokedex = especie.numero_de_pokedex
JOIN entrenador ON pokemon.id_entrenador = entrenador.id
WHERE especie.tipo_principal = 'fuego';

SELECT TIMEDIFF(NOW(6), @inicio) AS tiempo_de_la_consulta;
