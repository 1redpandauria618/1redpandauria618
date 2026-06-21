import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sqlite3
from math import pi, sqrt
# matplotlib stp
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM datatable')
data = cursor.fetchall()
# to float
longueur = [float(row[0]) for row in data]
periode = [float(row[1]) for row in data]
theorie = []
for row in data:
    theorie.append(2*pi*sqrt((float(row[0])/9.8)/100))
print(periode)
fig, ax = plt.subplots()
screen_distance = 1
ax.set_xlabel('longueur')
ax.set_ylabel('periode')
# render
ax.plot(longueur, periode, color='green')
ax.plot(longueur, theorie, color='red')

ax.legend()
ax.grid()
# sauver png
plt.savefig('graph2.png')
plt.show()