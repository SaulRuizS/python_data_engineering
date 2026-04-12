import psycopg2 as pcg2

connection_psycopg2 = pcg2.connect(database = "mydb",
                                   user = "postgres",
                                   host = 'localhost',
                                   password = "*******",
                                   port = 5432)
