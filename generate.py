import datetime
import os
import random

random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))

SIZES = [(1000, "1k"), (10000, "10k"), (100000, "100k")]

TYPES = ["fuego", "agua", "planta", "electrico", "roca", "volador",
         "psiquico", "hielo", "dragon", "siniestro", "acero", "hada",
         "normal", "lucha", "veneno", "tierra", "bicho", "fantasma"]

CATEGORIES = ["pocion", "baya", "piedra", "mochila", "tecnica", "tesoro", "llave"]

LOAD_ORDER = ["especie", "entrenador", "tipo_de_objeto", "pokemon"]

DROP_ORDER = list(reversed(LOAD_ORDER))

COLUMNS = {
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

POSTGRESQL_SCHEMA = """CREATE TABLE especie (
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

MYSQL_SCHEMA = """CREATE TABLE especie (
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

ENGINES = {
    "postgresql": {
        "schema": POSTGRESQL_SCHEMA,
        "before_load": "DO $$\n"
                       "DECLARE\n"
                       "    start_time TIMESTAMP := clock_timestamp();\n"
                       "BEGIN\n",
        "after_load": "    RAISE NOTICE 'Total load time: %',"
                      " clock_timestamp() - start_time;\n"
                      "END $$;\n",
    },
    "mysql": {
        "schema": MYSQL_SCHEMA,
        "before_load": "SET @start_time = NOW(6);\n"
                       "START TRANSACTION;\n",
        "after_load": "COMMIT;\n"
                      "SELECT TIMEDIFF(NOW(6), @start_time)"
                      " AS total_load_time;\n",
    },
}


def random_date():
    first_day = datetime.date(2000, 1, 1).toordinal()
    last_day = datetime.date(2025, 12, 31).toordinal()
    day = random.randint(first_day, last_day)
    return datetime.date.fromordinal(day).isoformat()


def stat():
    return random.randint(20, 200)


def literal(value):
    if value is None:
        return "NULL"
    if isinstance(value, int):
        return str(value)
    return f"'{value}'"


def insert_line(table, row):
    names = ", ".join(COLUMNS[table])
    values = ", ".join([literal(value) for value in row])
    return f"INSERT INTO {table} ({names}) VALUES ({values});"


def species_rows(n):
    rows = []
    for i in range(1, n + 1):
        health = stat()
        attack = stat()
        special_attack = stat()
        defense = stat()
        special_defense = stat()
        speed = stat()
        primary_type = random.choice(TYPES)
        secondary_type = random.choice(TYPES)
        if i == 1:
            pre_evolution = None
        else:
            pre_evolution = i - 1
        rows.append([i, f"especie_{i}",
                     health, attack, special_attack,
                     defense, special_defense, speed,
                     primary_type, secondary_type, pre_evolution])
    return rows


def trainer_rows(n):
    rows = []
    for i in range(1, n + 1):
        money = f"{random.uniform(0, 999999):.2f}"
        birth = random_date()
        rows.append([i, f"entrenador_{i}", money, birth])
    return rows


def item_type_rows(n):
    rows = []
    for i in range(1, n + 1):
        category = random.choice(CATEGORIES)
        rows.append([f"objeto_{i}", category])
    return rows


def pokemon_rows(n):
    rows = []
    for i in range(1, n + 1):
        obtained_on = random_date()
        species = random.randint(1, n)
        trainer = random.randint(1, n)
        if random.random() > 0.3:
            equipped = f"objeto_{random.randint(1, n)}"
        else:
            equipped = None
        rows.append([i, f"mote_{i}", obtained_on, species, trainer, equipped])
    return rows


GENERATORS = {
    "especie": species_rows,
    "entrenador": trainer_rows,
    "tipo_de_objeto": item_type_rows,
    "pokemon": pokemon_rows,
}


def write_load_file(path, engine, rows_per_table):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as file:
        for table in DROP_ORDER:
            file.write(f"DROP TABLE IF EXISTS {table};\n")
        file.write("\n")
        file.write(engine["schema"])
        file.write("\n")
        file.write(engine["before_load"])
        for table in LOAD_ORDER:
            for row in rows_per_table[table]:
                file.write("    " + insert_line(table, row) + "\n")
        file.write(engine["after_load"])


for n, label in SIZES:
    rows_per_table = {table: GENERATORS[table](n) for table in LOAD_ORDER}
    for engine_name, engine in ENGINES.items():
        path = os.path.join(BASE, engine_name, "data_loading", f"load_{label}.sql")
        write_load_file(path, engine, rows_per_table)
    print(f"Generated load_{label} for {', '.join(ENGINES)}")

print("Done")
