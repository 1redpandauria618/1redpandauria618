import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sqlite3
from math import pi, sqrt
# matplotlib stp
conn = sqlite3.connect('data3.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM datatable3')
data = cursor.fetchall()
# to float
mv = [float(row[0]) for row in data]
frequence = [float(row[1]) for row in data]
fig, ax = plt.subplots()
screen_distance = 1
ax.set_xlabel('frequence')
ax.set_ylabel('mv')
# render
ax.plot(frequence, mv, color='blue', marker='o')
ax.legend()
ax.grid()
# sauver png
plt.savefig('graph4.png')
plt.show()