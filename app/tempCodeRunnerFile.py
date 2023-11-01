import psycopg2

conn = psycopg2.connect(
    database="albums",
    user="postgres",
    password="$Redthong22",
    host="localhost",
    port=5433
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM messages")