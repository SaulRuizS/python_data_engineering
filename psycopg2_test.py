import psycopg2 as pcg2

connection = pcg2.connect(
    database = "mydb",
    user = "postgres",
    host = 'localhost',
    password = "********",
    port = 5432
)

cursor = connection.cursor()

cursor.execute("""
    --begin-sql
    CREATE TABLE postgresql_test_table (
        num_id  SERIAL          PRIMARY KEY
        ,num    INT
        ,info   VARCHAR(255)
    );
""")

cursor.execute("""
    --begin-sql
    INSERT INTO postgresql_test_table (
        num
        ,info
    )
    VALUES (
        %s
        ,%s
    );
""",(7,"Juan P. Montoya F1 Wins")
)

cursor.execute("""
    --begin-sql
    SELECT * FROM postgresql_test_table;
""")

cursor.fetchone()

connection.commit()

cursor.close()