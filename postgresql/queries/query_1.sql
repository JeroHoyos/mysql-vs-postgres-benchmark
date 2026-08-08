\timing on

SELECT pokemon.mote,
       especie.nombre_especie,
       especie.puntos_de_velocidad,
       entrenador.nombre_completo
FROM pokemon
JOIN especie ON pokemon.numero_de_pokedex = especie.numero_de_pokedex
JOIN entrenador ON pokemon.id_entrenador = entrenador.id
WHERE especie.tipo_principal = 'fuego';
