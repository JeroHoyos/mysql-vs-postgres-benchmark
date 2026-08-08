# MySQL

All times in milliseconds.

## Phase II. Loading

| Load | Rows per table | Time |
|---|---:|---:|
| Load 1 | 1,000 | 370.492 |
| Load 2 | 10,000 | 3596.290 |
| Load 3 | 100,000 | 35933.864 |

## Phase III. SQL queries

| Query | 1k | 10k | 100k |
|---|---:|---:|---:|
| Query 1 | 1.120 | 12.144 | 119.870 |
| Query 2 | 7.281 | 100.983 | 1043.776 |

## Phase IV. Queries in Python

Each measurement starts at the call to the database: open the connection, fetch the
tables the query needs, and resolve it with pandas.

| Step | 1k | 10k | 100k |
|---|---:|---:|---:|
| Fetch tables | 82.083 | 364.944 | 3595.773 |
| Query 1 | 48.183 | 323.382 | 3064.940 |
| Query 2 | 40.885 | 247.794 | 2543.436 |

## SQL against Python

| Query | Load | MySQL | Python |
|---|---|---:|---:|
| Query 1 | 1k | 1.120 | 48.183 |
| Query 1 | 10k | 12.144 | 323.382 |
| Query 1 | 100k | 119.870 | 3064.940 |
| Query 2 | 1k | 7.281 | 40.885 |
| Query 2 | 10k | 100.983 | 247.794 |
| Query 2 | 100k | 1043.776 | 2543.436 |
