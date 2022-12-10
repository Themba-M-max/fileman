import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="fileman",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (email varchar (320) PRIMARY KEY,'
                                 'password varchar (255) NOT NULL);'
                                 )

# Insert data into the table

# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('A Tale of Two Cities',
#              'Charles Dickens',
#              489,
#              'A great classic!')
#             )


# cur.execute('INSERT INTO users (email, password)'
#             'VALUES (%s, %s)',
#             ('test@email.com',
#              'password')
#             )



conn.commit()

cur.close()
conn.close()