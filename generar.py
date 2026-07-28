import datetime
import os
import random

random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))

TAMANOS = [(1000, "1k"), (10000, "10k"), (100000, "100k")]

TIPOS = ["fuego", "agua", "planta", "electrico", "roca", "volador",
         "psiquico", "hielo", "dragon", "siniestro", "acero", "hada",
         "normal", "lucha", "veneno", "tierra", "bicho", "fantasma"]

CATEGORIAS = ["pocion", "baya", "piedra", "mochila", "tecnica", "tesoro", "llave"]

ORDEN_DE_CARGA = ["especie", "entrenador", "tipo_de_objeto", "pokemon"]

ORDEN_DE_BORRADO = list(reversed(ORDEN_DE_CARGA))

COLUMNAS = {
    "especie": ["numero_de_pokedex", "nombre_especie",
                "puntos_de_salud", "puntos_de_ataque", "puntos_de_ataque_esp",
                "puntos_de_defensa", "puntos_de_defensa_esp", "puntos_de_velocidad",
                "tipo_principal", "tipo_secundario", "pre_evolucion"],
    "entrenador": ["id", "nombre_completo",
                   "dinero_disponible", "dia_de_nacimiento"],
    "tipo_de_objeto": ["nombre", "categoria"],
    "pokemon": ["codigo", "mote", "fecha_de_obtencion",
                "numero_de_pokedex", "id_entrenador", "nombre_objeto"],
}

ESQUEMA_POSTGRESQL = """CREATE TABLE especie (
    numero_de_pokedex INTEGER PRIMARY KEY,
    nombre_especie VARCHAR(60) NOT NULL,
    puntos_de_salud INTEGER NOT NULL,
    puntos_de_ataque INTEGER NOT NULL,
    puntos_de_ataque_esp INTEGER NOT NULL,
    puntos_de_defensa INTEGER NOT NULL,
    puntos_de_defensa_esp INTEGER NOT NULL,
    puntos_de_velocidad INTEGER NOT NULL,
    tipo_principal VARCHAR(20) NOT NULL,
    tipo_secundario VARCHAR(20),
    pre_evolucion INTEGER,
    FOREIGN KEY (pre_evolucion) REFERENCES especie (numero_de_pokedex)
);

CREATE TABLE entrenador (
    id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    dinero_disponible NUMERIC(10,2) NOT NULL,
    dia_de_nacimiento DATE NOT NULL
);

CREATE TABLE tipo_de_objeto (
    nombre VARCHAR(50) PRIMARY KEY,
    categoria VARCHAR(50) NOT NULL
);

CREATE TABLE pokemon (
    codigo SERIAL PRIMARY KEY,
    mote VARCHAR(60) NOT NULL,
    fecha_de_obtencion DATE NOT NULL,
    numero_de_pokedex INTEGER NOT NULL,
    id_entrenador INTEGER NOT NULL,
    nombre_objeto VARCHAR(50),
    FOREIGN KEY (numero_de_pokedex) REFERENCES especie (numero_de_pokedex),
    FOREIGN KEY (id_entrenador) REFERENCES entrenador (id),
    FOREIGN KEY (nombre_objeto) REFERENCES tipo_de_objeto (nombre)
);
"""

ESQUEMA_MYSQL = """CREATE TABLE especie (
    numero_de_pokedex INT PRIMARY KEY,
    nombre_especie VARCHAR(60) NOT NULL,
    puntos_de_salud INT NOT NULL,
    puntos_de_ataque INT NOT NULL,
    puntos_de_ataque_esp INT NOT NULL,
    puntos_de_defensa INT NOT NULL,
    puntos_de_defensa_esp INT NOT NULL,
    puntos_de_velocidad INT NOT NULL,
    tipo_principal VARCHAR(20) NOT NULL,
    tipo_secundario VARCHAR(20),
    pre_evolucion INT,
    FOREIGN KEY (pre_evolucion) REFERENCES especie (numero_de_pokedex)
);

CREATE TABLE entrenador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    dinero_disponible DECIMAL(10,2) NOT NULL,
    dia_de_nacimiento DATE NOT NULL
);

CREATE TABLE tipo_de_objeto (
    nombre VARCHAR(50) PRIMARY KEY,
    categoria VARCHAR(50) NOT NULL
);

CREATE TABLE pokemon (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    mote VARCHAR(60) NOT NULL,
    fecha_de_obtencion DATE NOT NULL,
    numero_de_pokedex INT NOT NULL,
    id_entrenador INT NOT NULL,
    nombre_objeto VARCHAR(50),
    FOREIGN KEY (numero_de_pokedex) REFERENCES especie (numero_de_pokedex),
    FOREIGN KEY (id_entrenador) REFERENCES entrenador (id),
    FOREIGN KEY (nombre_objeto) REFERENCES tipo_de_objeto (nombre)
);
"""

MOTORES = {
    "postgreSQL": {
        "esquema": ESQUEMA_POSTGRESQL,
        "antes_de_la_carga": "DO $$\n"
                             "DECLARE\n"
                             "    inicio TIMESTAMP := clock_timestamp();\n"
                             "BEGIN\n",
        "despues_de_la_carga": "    RAISE NOTICE 'Tiempo total de la carga: %',"
                               " clock_timestamp() - inicio;\n"
                               "END $$;\n",
    },
    "mysql": {
        "esquema": ESQUEMA_MYSQL,
        "antes_de_la_carga": "SET @inicio = NOW(6);\n"
                             "START TRANSACTION;\n",
        "despues_de_la_carga": "COMMIT;\n"
                               "SELECT TIMEDIFF(NOW(6), @inicio)"
                               " AS tiempo_total_de_la_carga;\n",
    },
}


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


def linea_insert(tabla, fila):
    nombres = ", ".join(COLUMNAS[tabla])
    valores = ", ".join([literal(valor) for valor in fila])
    return f"INSERT INTO {tabla} ({nombres}) VALUES ({valores});"


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


GENERADORES = {
    "especie": filas_especie,
    "entrenador": filas_entrenador,
    "tipo_de_objeto": filas_tipo_de_objeto,
    "pokemon": filas_pokemon,
}


def escribir(ruta, motor, filas_por_tabla):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as archivo:
        for tabla in ORDEN_DE_BORRADO:
            archivo.write(f"DROP TABLE IF EXISTS {tabla};\n")
        archivo.write("\n")
        archivo.write(motor["esquema"])
        archivo.write("\n")
        archivo.write(motor["antes_de_la_carga"])
        for tabla in ORDEN_DE_CARGA:
            for fila in filas_por_tabla[tabla]:
                archivo.write("    " + linea_insert(tabla, fila) + "\n")
        archivo.write(motor["despues_de_la_carga"])


for n, etiqueta in TAMANOS:
    filas_por_tabla = {tabla: GENERADORES[tabla](n) for tabla in ORDEN_DE_CARGA}
    for nombre_motor, motor in MOTORES.items():
        ruta = os.path.join(BASE, nombre_motor, "carga_de_datos",
                            f"carga_{etiqueta}.sql")
        escribir(ruta, motor, filas_por_tabla)
    print(f"Generada carga_{etiqueta} para {', '.join(MOTORES)}")

print("Listo")
