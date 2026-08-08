# PostgreSQL

All times in milliseconds.

## Phase II. Loading

| Load | Rows per table | Time |
|---|---:|---:|
| Load 1 | 1,000 | 226.006 |
| Load 2 | 10,000 | 2252.994 |
| Load 3 | 100,000 | 25784.750 |

## Phase III. SQL queries

| Query | 1k | 10k | 100k |
|---|---:|---:|---:|
| Query 1 | 2.928 | 6.994 | 52.796 |
| Query 2 | 8.393 | 82.338 | 1058.145 |

## Phase IV. Queries in Python

Each measurement starts at the call to the database: open the connection, fetch the
tables the query needs, and resolve it with pandas.

| Step | 1k | 10k | 100k |
|---|---:|---:|---:|
| Fetch tables | 95.952 | 152.862 | 1222.129 |
| Query 1 | 30.413 | 125.677 | 1184.717 |
| Query 2 | 27.445 | 108.340 | 997.931 |

## SQL against Python

| Query | Load | PostgreSQL | Python |
|---|---|---:|---:|
| Query 1 | 1k | 2.928 | 30.413 |
| Query 1 | 10k | 6.994 | 125.677 |
| Query 1 | 100k | 52.796 | 1184.717 |
| Query 2 | 1k | 8.393 | 27.445 |
| Query 2 | 10k | 82.338 | 108.340 |
| Query 2 | 100k | 1058.145 | 997.931 |
