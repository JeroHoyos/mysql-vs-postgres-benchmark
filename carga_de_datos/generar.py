import random
import os
import datetime

random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))

TAMANOS = [(1000, "1k"), (10000, "10k"), (100000, "100k")]

TIPOS = ["fuego", "agua", "planta", "electrico", "roca", "volador",
         "psiquico", "hielo", "dragon", "siniestro", "acero", "hada",
         "normal", "lucha", "veneno", "tierra", "bicho", "fantasma"]

CATEGORIAS = ["pocion", "baya", "piedra", "mochila", "tecnica", "tesoro", "llave"]

COLUMNAS_ESPECIE = ["numero_de_pokedex", "nombre_especie",
                    "puntos_de_salud", "puntos_de_ataque", "puntos_de_ataque_esp",
                    "puntos_de_defensa", "puntos_de_defensa_esp", "puntos_de_velocidad",
                    "tipo_principal", "tipo_secundario", "pre_evolucion"]

COLUMNAS_ENTRENADOR = ["id", "nombre_completo",
                       "dinero_disponible", "dia_de_nacimiento"]

COLUMNAS_TIPO_DE_OBJETO = ["nombre", "categoria"]

COLUMNAS_POKEMON = ["codigo", "mote", "fecha_de_obtencion",
                    "numero_de_pokedex", "id_entrenador", "nombre_objeto"]


def fecha():
    primer_dia = datetime.date(2000, 1, 1).toordinal()
    ultimo_dia = datetime.date(2025, 12, 31).toordinal()
    dia = random.randint(primer_dia, ultimo_dia)
    return datetime.date.fromordinal(dia).isoformat()


def estadistica():
    return random.randint(20, 200)


def literal(valor):
    if valor is None:
        return "NULL"
    if isinstance(valor, int):
        return str(valor)
    return f"'{valor}'"


def linea_insert(tabla, columnas, fila):
    nombres = ", ".join(columnas)
    valores = ", ".join([literal(valor) for valor in fila])
    return f"INSERT INTO {tabla} ({nombres}) VALUES ({valores});"


def escribir(carpeta, tabla, columnas, filas):
    ruta = os.path.join(carpeta, f"{tabla}.txt")
    with open(ruta, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(f"-- {tabla}: {len(filas)} filas\n")
        archivo.write("BEGIN;\n")
        for fila in filas:
            archivo.write(linea_insert(tabla, columnas, fila) + "\n")
        archivo.write("COMMIT;\n")


def filas_especie(n):
    filas = []
    for i in range(1, n + 1):
        salud = estadistica()
        ataque = estadistica()
        ataque_esp = estadistica()
        defensa = estadistica()
        defensa_esp = estadistica()
        velocidad = estadistica()
        tipo_principal = random.choice(TIPOS)
        tipo_secundario = random.choice(TIPOS)
        if i == 1:
            pre_evolucion = None
        else:
            pre_evolucion = i - 1
        filas.append([i, f"especie_{i}",
                      salud, ataque, ataque_esp,
                      defensa, defensa_esp, velocidad,
                      tipo_principal, tipo_secundario, pre_evolucion])
    return filas


def filas_entrenador(n):
    filas = []
    for i in range(1, n + 1):
        dinero = f"{random.uniform(0, 999999):.2f}"
        nacimiento = fecha()
        filas.append([i, f"entrenador_{i}", dinero, nacimiento])
    return filas


def filas_tipo_de_objeto(n):
    filas = []
    for i in range(1, n + 1):
        categoria = random.choice(CATEGORIAS)
        filas.append([f"objeto_{i}", categoria])
    return filas


def filas_pokemon(n):
    filas = []
    for i in range(1, n + 1):
        obtenido_el = fecha()
        especie = random.randint(1, n)
        entrenador = random.randint(1, n)
        if random.random() > 0.3:
            equipado = f"objeto_{random.randint(1, n)}"
        else:
            equipado = None
        filas.append([i, f"mote_{i}", obtenido_el, especie, entrenador, equipado])
    return filas


def generar(n, carpeta):
    os.makedirs(carpeta, exist_ok=True)
    escribir(carpeta, "especie", COLUMNAS_ESPECIE, filas_especie(n))
    escribir(carpeta, "entrenador", COLUMNAS_ENTRENADOR, filas_entrenador(n))
    escribir(carpeta, "tipo_de_objeto", COLUMNAS_TIPO_DE_OBJETO, filas_tipo_de_objeto(n))
    escribir(carpeta, "pokemon", COLUMNAS_POKEMON, filas_pokemon(n))


for n, etiqueta in TAMANOS:
    carpeta = os.path.join(BASE, f"carga_{etiqueta}")
    generar(n, carpeta)
    print(f"Generada carga_{etiqueta}")

print("Listo")
