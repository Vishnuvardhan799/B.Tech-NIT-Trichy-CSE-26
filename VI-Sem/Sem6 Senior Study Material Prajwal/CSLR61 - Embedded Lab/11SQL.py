import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("INSERT INTO `users` (`rno`, `name`) VALUES ('106121092', 'Prajwal')")
c.commit()