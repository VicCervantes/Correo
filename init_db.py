import sqlite3

conn = sqlite3.connect('logs.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS user_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        user_agent TEXT,
        timestamp TEXT
    )
''')

conn.commit()

print("Base de datos y tabla creadas con éxito.")

conn.close() 

# Este comando sirve para limpiar toda la BD, se comenta lo anterior "#" y se ejecuta con python init_db.py para eliminar todos los registros
# DELETE FROM user_logs;