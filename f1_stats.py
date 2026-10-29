import psycopg2 as pcg2
import pandas as pd
#import plotly.express as px

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
        driver.name
        --,season_driver_standing.year
        ,season_driver_standing.points
        --,COUNT(*) FILTER (WHERE race_result.position_display_order >= 3) AS podiums
        ,COUNT(*) FILTER (WHERE race_result.position_number = 1) AS wins
    FROM driver
    LEFT JOIN season_driver_standing ON driver.id = season_driver_standing.driver_id
    LEFT JOIN race_result ON driver.id = race_result.driver_id
    WHERE driver.date_of_birth >= '1989-01-01'
            --AND driver.total_race_wins > 0
            AND season_driver_standing.year = 2026
            --AND race_result.position_number IS NOT NULL
    GROUP BY driver.name, season_driver_standing.points
    ORDER BY season_driver_standing.points ASC
    ;
""")

data = cursor.fetchall()

df = pd.DataFrame(data, columns=['Driver', 'Points', 'Wins'])

print(df)

#print(data)

connection.commit()

cursor.close()