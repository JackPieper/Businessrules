import psycopg2

conn = psycopg2.connect(host="localhost", database="op=op voordeelshop", user="postgres", password="PostGres")
cursor = conn.cursor()

cursor.execute("")
conn.commit()