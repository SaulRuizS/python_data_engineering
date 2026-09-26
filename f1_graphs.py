import psycopg2 as pcg2
import pandas as pd
import plotly.express as px

connection = pcg2.connect(
    database = "f1_database",
    user = "postgres",
    host = 'localhost',
    password = "postgresql",
    port = 5432
)

cursor = connection.cursor()

cursor.execute("""
    --begin-sql
    SELECT
        season_driver_standing.year
        ,driver.name
        ,season_driver_standing.points
    FROM driver
    LEFT JOIN season_driver_standing ON driver.id = season_driver_standing.driver_id
    WHERE driver.date_of_birth >= '1980-01-01'
        --AND driver.total_race_wins > 0
        AND season_driver_standing.year = 2026
    ORDER BY season_driver_standing.points ASC;
""")

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['year', 'name', 'points'])

graph = px.line(df, x="name", y="points", title="Season 2026 per driver")

graph.show()

print(df)

connection.commit()

cursor.close()