import sqlite3

conn = sqlite3.connect('logs.db')
c = conn.cursor()

# Borrar todos los registros de la tabla
c.execute("DELETE FROM user_logs")

conn.commit()
print("Registros eliminados con éxito.")
conn.close()
