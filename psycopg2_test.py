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
        name
        ,date_of_birth
        ,date_of_death
        ,place_of_birth
        ,total_race_starts
        ,total_podiums
        ,total_race_wins
        ,total_points
        ,total_pole_positions
        ,total_fastest_laps
        ,total_grand_slams
    FROM driver
    WHERE date_of_birth >= '1996-01-01'
    ORDER BY date_of_birth ASC;
""")

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['name', 'date_of_birth', 'date_of_death', 'place_of_birth', 'total_race_starts', 'total_podiums', 'total_race_wins', 'total_points', 'total_pole_positions', 'total_fastest_laps', 'total_grand_slams'])

graph = px.line(df, x="name", y="total_race_wins", title="Podiums per driver")

graph.show()

#print(df)

connection.commit()

cursor.close()