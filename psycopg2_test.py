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
        --,date_of_birth
        --,date_of_death
        --,place_of_birth
        --,total_race_starts
        ,driver.total_podiums
        ,driver.total_race_wins
        --,total_points
        ,driver.total_pole_positions
        --,total_fastest_laps
        --,total_grand_slams
        ,season_driver_standing.points
    FROM driver
    LEFT JOIN season_driver_standing ON driver.id = season_driver_standing.driver_id
    WHERE driver.date_of_birth >= '1996-01-01'
        AND driver.total_race_wins > 0
        AND season_driver_standing.year = 2024
    ORDER BY season_driver_standing.points DESC;
""")

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['year', 'name', 'total_podiums', 'total_race_wins', 'total_pole_positions', 'points'])

#graph = px.line(df, x="name", y="total_race_wins", title="Race Wins per driver")

#graph.show()

print(df)

connection.commit()

cursor.close()