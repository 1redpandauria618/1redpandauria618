import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sqlite3
# matplotlib stp
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM datatable')
data = cursor.fetchall()
print(data)
longeur = [row[0] for row in data]
print(longeur)
periode = [row[1] for row in data]
print(periode)
fig, ax = plt.subplots()
screen_distance = 1
ax.set_xlabel('longeur')
ax.set_ylabel('periode')
# render
ax.plot(longeur, periode)
ax.legend()
ax.grid()
# sauver png
plt.savefig('graph.png')