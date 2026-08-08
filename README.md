# MySQL vs PostgreSQL

> Performance comparison of MySQL and PostgreSQL on insertion and query workloads, with pandas as an in-memory reference.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

## Contents

- [Schema](#schema)
- [Phase I. Schema implementation](#phase-i-schema-implementation)
- [Experimental setup](#experimental-setup)
- [Phase II. Data loading](#phase-ii-data-loading)
- [Phase III. SQL queries](#phase-iii-sql-queries)
- [Phase IV. Running the queries from Python](#phase-iv-running-the-queries-from-python)
- [Overall results and conclusions](#overall-results-and-conclusions)
- [Repository layout](#repository-layout)

---

## Schema

Four connected entities were selected from the relations built in the previous
assignment: **Especie**, **Pokémon**, **Entrenador** and **Tipo de Objeto**.

Table and column names are kept in Spanish throughout, because the loaded data, the
recorded timings and the appendix screenshots all depend on them.

![Entity-relationship model](docs/imgs/schema.png)

## Phase I. Schema implementation

The database was implemented in both MySQL and PostgreSQL from the ER model.

### MySQL

```sql
CREATE TABLE especie (
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
```

### PostgreSQL

The only differences are the integer types and the auto-increment keys.

```sql
CREATE TABLE especie (
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
```

## Experimental setup

Every timing reported here was measured on the same machine, so the results are
comparable with one another.

| Component | Specification |
|---|---|
| Processor | Intel Core i5, 4 cores |
| Graphics | Intel Iris Plus Graphics 655 |
| Memory | 8 GB LPDDR3 |

Both engines receive byte-identical rows: [generate.py](generate.py) builds the rows
once per load size and writes the same set into each engine's `.sql` file, so only the
DDL and the timing wrapper differ. The generator is seeded, so runs are reproducible.

## Phase II. Data loading

### Population code

The data was generated with a Python script. For each load size the script writes a
`.sql` file that inserts n rows and records the execution time.

Below is the loading block for each engine, where the ellipsis stands for the n rows
repeated in each table.

**MySQL**

```sql
SET @inicio = NOW(6);
START TRANSACTION;
    INSERT INTO especie (numero_de_pokedex, nombre_especie, puntos_de_salud, ...) VALUES (1, 'especie_1', 118, ...);
    ...
    INSERT INTO entrenador (id, nombre_completo, dinero_disponible, dia_de_nacimiento) VALUES (1, 'entrenador_1', '523847.19', '2011-04-23');
    ...
    INSERT INTO tipo_de_objeto (nombre, categoria) VALUES ('objeto_1', 'pocion');
    ...
    INSERT INTO pokemon (codigo, mote, fecha_de_obtencion, numero_de_pokedex, id_entrenador, nombre_objeto) VALUES (1, 'mote_1', '2015-08-12', 5, 3, 'objeto_7');
    ...
COMMIT;
SELECT TIMEDIFF(NOW(6), @inicio) AS tiempo_total_de_la_carga;
```

**PostgreSQL**

```sql
DO $$
DECLARE
    inicio TIMESTAMP := clock_timestamp();
BEGIN
    INSERT INTO especie (numero_de_pokedex, nombre_especie, puntos_de_salud, ...) VALUES (1, 'especie_1', 118, ...);
    ...
    INSERT INTO entrenador (id, nombre_completo, dinero_disponible, dia_de_nacimiento) VALUES (1, 'entrenador_1', '523847.19', '2011-04-23');
    ...
    INSERT INTO tipo_de_objeto (nombre, categoria) VALUES ('objeto_1', 'pocion');
    ...
    INSERT INTO pokemon (codigo, mote, fecha_de_obtencion, numero_de_pokedex, id_entrenador, nombre_objeto) VALUES (1, 'mote_1', '2015-08-12', 5, 3, 'objeto_7');
    ...
    RAISE NOTICE 'Tiempo total de la carga: %', clock_timestamp() - inicio;
END $$;
```

### Insertion times

Three insertion tests were run on each DBMS, with 1,000, 10,000 and 100,000 rows per
table, measuring the time taken in each case.

| Load test | MySQL | PostgreSQL |
|---|---:|---:|
| 1,000 rows | 0.370492 s | 0.226006 s |
| 10,000 rows | 3.596290 s | 2.252994 s |
| 100,000 rows | 35.933864 s | 25.784750 s |

![Insertion time by load size](docs/imgs/insertion.png)

PostgreSQL was significantly faster in all three insertion tests, between 1.4 and 1.6
times faster than MySQL, and the advantage held at every load size.

## Phase III. SQL queries

Both queries are identical in MySQL and PostgreSQL, so only one version of each is
shown.

### Query 1

Returns the pokémon whose primary type is fire, along with their species name and
speed and the name of the trainer who owns them. It joins `pokemon`, `especie` and
`entrenador`.

```sql
SELECT pokemon.mote,
       especie.nombre_especie,
       especie.puntos_de_velocidad,
       entrenador.nombre_completo
FROM pokemon
JOIN especie ON pokemon.numero_de_pokedex = especie.numero_de_pokedex
JOIN entrenador ON pokemon.id_entrenador = entrenador.id
WHERE especie.tipo_principal = 'fuego';
```

First five rows of the result, on the 100,000-row load:

| mote | nombre_especie | puntos_de_velocidad | nombre_completo |
|---|---|---:|---|
| mote_39 | especie_73737 | 147 | entrenador_90283 |
| mote_65 | especie_68064 | 107 | entrenador_1986 |
| mote_70 | especie_35863 | 39 | entrenador_68181 |
| mote_71 | especie_69590 | 88 | entrenador_27336 |
| mote_78 | especie_81380 | 54 | entrenador_61988 |

The query imposes no ordering, so these are simply the first rows the engine returns.

![Query 1, PostgreSQL vs MySQL](docs/imgs/engines_query_1.png)

MySQL was ahead on the first load, 1.12 ms against 2.93 ms, but PostgreSQL caught up on
the second and third. On the last one its advantage was clearest: 52.8 ms against
120 ms, more than twice as fast.

### Query 2

Counts how many pokémon each trainer has per category of equipped item. It groups by
trainer and category and orders from highest to lowest count, breaking ties by trainer
name.

```sql
SELECT entrenador.nombre_completo,
       tipo_de_objeto.categoria,
       COUNT(*) AS total_pokemon
FROM pokemon
JOIN entrenador ON pokemon.id_entrenador = entrenador.id
JOIN tipo_de_objeto ON pokemon.nombre_objeto = tipo_de_objeto.nombre
GROUP BY entrenador.nombre_completo, tipo_de_objeto.categoria
ORDER BY total_pokemon DESC, entrenador.nombre_completo;
```

First five rows of the result, on the 100,000-row load:

| nombre_completo | categoria | total_pokemon |
|---|---|---:|
| entrenador_66533 | piedra | 4 |
| entrenador_11979 | llave | 3 |
| entrenador_12463 | pocion | 3 |
| entrenador_12501 | tesoro | 3 |
| entrenador_13494 | tesoro | 3 |

Here the ordering is fixed by the query, so these are the trainers with the most
pokémon in a single item category.

![Query 2, PostgreSQL vs MySQL](docs/imgs/engines_query_2.png)

The two engines were much closer than in the previous query. MySQL was faster at 1,000
rows, 7.28 ms against 8.39 ms, and also at 100,000 rows, where it recorded 1044 ms
against 1058 ms — barely a 1.4% difference. At 10,000 rows PostgreSQL was the faster
one, 82.3 ms against 101 ms. No clear advantage between engines was found.

## Phase IV. Running the queries from Python

Each query opens its own connection to the DBMS, fetches only the tables it needs with
`SELECT * FROM tabla`, and combines the data in application code. The clock covers that
entire path, so the measured time is comparable to what the SQL client reports for the
equivalent query.

### Connection and timing

The connection and timing code is identical for MySQL and PostgreSQL. The only thing
that changes between them is the connection string.

```python
# MySQL
CONNECTION = "mysql+pymysql://root:@localhost:3306/{database}"
# PostgreSQL
CONNECTION = "postgresql+psycopg2://postgres:1234@localhost:5432/{database}"
```

The rest of the code is common to both engines.

```python
import os
import time
import pandas as pd
from sqlalchemy import create_engine

BASE = os.path.dirname(os.path.abspath(__file__))
TABLES = ["especie", "entrenador", "tipo_de_objeto", "pokemon"]
DATABASES = ["pokemon_1k", "pokemon_10k", "pokemon_100k"]
CONNECTION = "Depends on the engine"


def fetch_tables(url, tables=TABLES):
    with create_engine(url).connect() as connection:
        return {table: pd.read_sql(f"SELECT * FROM {table}", connection)
                for table in tables}


def time_it(function, argument):
    start = time.perf_counter()
    result = function(argument)
    return result, (time.perf_counter() - start) * 1000


measurements = []

for database_name in DATABASES:
    url = CONNECTION.format(database=database_name)
    tables, fetch_time = time_it(fetch_tables, url)
    result_1, time_1 = time_it(query_1, url)
    result_2, time_2 = time_it(query_2, url)

    fetched_rows = sum(len(table) for table in tables.values())
    measurements.append([database_name, "fetch tables", fetch_time, fetched_rows])
    measurements.append([database_name, "query 1", time_1, len(result_1)])
    measurements.append([database_name, "query 2", time_2, len(result_2)])

times = pd.DataFrame(measurements,
                     columns=["load", "step", "milliseconds", "rows"])
times.to_csv(os.path.join(BASE, "times.csv"), index=False)
```

### Solving the queries in Python

pandas was used for the Python side, one of the most widely used data-processing
libraries in data science.

```python
def query_1(url):
    tables = fetch_tables(url, ["pokemon", "especie", "entrenador"])
    with_species = tables["pokemon"].merge(tables["especie"],
                                           on="numero_de_pokedex")
    with_trainer = with_species.merge(tables["entrenador"],
                                      left_on="id_entrenador", right_on="id")
    fire_type = with_trainer[with_trainer["tipo_principal"] == "fuego"]
    return fire_type[["mote", "nombre_especie",
                      "puntos_de_velocidad", "nombre_completo"]]


def query_2(url):
    tables = fetch_tables(url, ["pokemon", "entrenador", "tipo_de_objeto"])
    with_trainer = tables["pokemon"].merge(tables["entrenador"],
                                           left_on="id_entrenador", right_on="id")
    with_item = with_trainer.merge(tables["tipo_de_objeto"],
                                   left_on="nombre_objeto", right_on="nombre")
    counts = with_item.groupby(["nombre_completo", "categoria"]).size()
    counts = counts.reset_index(name="total_pokemon")
    return counts.sort_values(["total_pokemon", "nombre_completo"],
                              ascending=[False, True])
```

### SQL against Python

Query 1, each engine against pandas:

![Query 1, MySQL vs Python](docs/imgs/query_1_mysql_vs_python.png)

![Query 1, PostgreSQL vs Python](docs/imgs/query_1_postgresql_vs_python.png)

In both comparisons the database engines beat the specialised Python library by a wide
margin.

Query 2, the same comparison:

![Query 2, MySQL vs Python](docs/imgs/query_2_mysql_vs_python.png)

For MySQL the advantage held, though by a smaller margin than in query 1.

![Query 2, PostgreSQL vs Python](docs/imgs/query_2_postgresql_vs_python.png)

PostgreSQL had a much harder time. It kept the lead on the first two loads, 8.39 ms
against 27.4 ms and 82.3 ms against 108 ms, but the margin kept narrowing and on the
100,000-row load pandas came out ahead, 998 ms against 1058 ms. It is the only scenario
in the whole assignment where the Python library beat a database engine.

## Overall results and conclusions

Query response times by scenario and load, in milliseconds:

| Query | Load | MySQL | PostgreSQL | Python from MySQL | Python from Pg |
|---|---|---:|---:|---:|---:|
| Query 1 | 1,000 | 1.120 | 2.928 | 48.183 | 30.413 |
| Query 1 | 10,000 | 12.144 | 6.994 | 323.382 | 125.677 |
| Query 1 | 100,000 | 119.870 | 52.796 | 3064.940 | 1184.717 |
| Query 2 | 1,000 | 7.281 | 8.393 | 40.885 | 27.445 |
| Query 2 | 10,000 | 100.983 | 82.338 | 247.794 | 108.340 |
| Query 2 | 100,000 | 1043.776 | 1058.145 | 2543.436 | 997.931 |

For query 1 the best scenario was PostgreSQL, which won at 10,000 and 100,000 rows, and
the worst was calling from Python against MySQL.

For query 2 the two engines were practically tied, and the best time on the largest
load belonged to neither of them but to Python from PostgreSQL, at 998 ms. The worst
scenario was again Python from MySQL, across all three loads.

Both queries on a logarithmic scale:

![SQL query times](docs/imgs/sql_queries.png)

The gap between engines is sharper in query 1, where from 10,000 rows on the PostgreSQL
curve sits clearly below the MySQL one, while in query 2 the two curves nearly overlap.
Query 2 is also roughly an order of magnitude more expensive than query 1 on the
100,000-row load, which is explained by the `GROUP BY` and `ORDER BY` it has to
resolve.

Both queries summed:

![Both queries summed](docs/imgs/overall.png)

At 1,000 rows MySQL is the best, 8.4 ms against 11 ms. As the load grows PostgreSQL
moves ahead, comfortably at first — 89 ms against 113 ms — and then only barely, 1.11 s
against 1.16 s. The worst result at all three loads is calling MySQL from Python.

**Conclusions**

- For pure `JOIN` work PostgreSQL was superior, more than twice as fast as MySQL on the
  100,000-row load.
- For `GROUP BY` and `ORDER BY` (query 2) the two engines came out even, so no winner
  can be declared.
- Calling from Python together with specialised libraries did not turn out to be
  optimal; running a script directly inside the DBMS was preferable. The one exception
  was query 2 over 100,000 rows read from PostgreSQL, where pandas edged past the
  engine by a narrow margin.
- For querying data, database management systems showed a general advantage over Python
  scripts.
- For insertion, PostgreSQL was significantly better than MySQL at all three load
  sizes.

## Repository layout

```
├── docs/
│   ├── benchmark_analysis.ipynb   # Notebook that produces the figures
│   └── imgs/                      # Figures and appendix screenshots
├── mysql/
│   ├── README.md                  # Measured times
│   ├── schemas.txt
│   ├── queries.txt
│   ├── queries/                   # The two queries, one file each
│   ├── data_loading/              # Generated load files (git-ignored)
│   └── python/queries.py          # The same queries solved with pandas
├── postgresql/                    # Same layout as mysql/
└── generate.py                    # Synthetic data generator
```

Reproducing the benchmarks:

```bash
python generate.py                          # writes the .sql load files
# run each data_loading/load_*.sql in its engine
python postgresql/python/queries.py         # phase IV, PostgreSQL
python mysql/python/queries.py              # phase IV, MySQL
```
