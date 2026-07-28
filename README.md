# MySQL vs PostgreSQL

> Comparativa de rendimiento MySQL vs. PostgreSQL en operaciones de inserción y consulta, usando pandas como referencia en memoria.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

## Esquema

![esquema entidad-relación](docs/imgs/esquema.png)


## Fases

| Fase | Qué se mide |
| ---- | ----------- |
| I | Implementación de los esquemas en ambos motores |
| II | Carga de datos con 1k, 10k y 100k filas por tabla |
| III | Dos consultas en SQL sobre cada carga |
| IV | Las mismas dos consultas resueltas con pandas |


## Resultados

![Consulta 1: PostgreSQL contra MySQL](docs/imgs/motores_consulta_1.png)

![Consulta 2: PostgreSQL contra MySQL](docs/imgs/motores_consulta_2.png)

PostgreSQL gana las seis medidas de consulta y carga entre 3,5 y 4,3 veces más rápido. El
detalle de cada motor está en [postgreSQL/README.md](postgreSQL/README.md) y
[mysql/README.md](mysql/README.md), y las gráficas salen de
[docs/analisis_benchmark.ipynb](docs/analisis_benchmark.ipynb).

## Estructura

```
├── docs/            # Informe en LaTeX, notebook de análisis y figuras
├── postgreSQL/      # Esquema, consultas, cargas y la versión en pandas
├── mysql/           # Lo mismo para MySQL
└── generar.py       # Generador de los datos sintéticos
```

