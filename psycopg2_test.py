import psycopg2 as pcg2

connection = pcg2.connect(
    database = "f1_database",
    user = "postgres",
    host = 'localhost',
    password = "Mosmostaza1?",
    port = 5432
)

cursor = connection.cursor()

# cursor.execute("""
    # --begin-sql
    # CREATE TABLE postgresql_test_table (
        # num_id  SERIAL          PRIMARY KEY
        # ,num    INT
        # ,info   VARCHAR(255)
    # );
# """)
# 
# cursor.execute("""
    # --begin-sql
    # INSERT INTO postgresql_test_table (
        # num
        # ,info
    # )
    # VALUES (
        # %s
        # ,%s
    # );
# """,(7,"Juan P. Montoya F1 Wins")
# )

cursor.execute("""
    --begin-sql
    SELECT COUNT(*) FROM driver
    WHERE total_race_wins >= 20;
""")

print(cursor.fetchmany(100))

connection.commit()

cursor.close()