import duckdb

con = duckdb.connect("data/jikan.duckdb")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

con.execute("""
    CREATE TABLE IF NOT EXISTS raw.seasons_anime (
        mal_id          INTEGER,
        year            INTEGER,
        season          VARCHAR,
        payload         VARCHAR,
        source_endpoint VARCHAR,
        ingested_at     TIMESTAMP
    )
""")

print(con.execute("SELECT COUNT(*) FROM raw.seasons_anime").fetchall())

import json

with open("data/raw/anime_2026_winter.json", encoding="utf-8") as f:
    records = json.load(f)

print(len(records))
print(records[0]["mal_id"], records[0]["title"])

con.close()