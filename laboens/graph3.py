import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sqlite3
from math import pi, sqrt
# matplotlib stp
conn = sqlite3.connect('data2.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM datatable2')
data = cursor.fetchall()
# to float
periode_pendule = [float(row[0]) for row in data]
amplitude = [float(row[1]) for row in data]
theorie = []
for row in data:
    theorie.append(2 * pi * sqrt(1.005 / 9.81) * (1 + float(row[1])**2 / 16))
fig, ax = plt.subplots()
screen_distance = 1
ax.set_xlabel('amplitude')
ax.set_ylabel('periode_pendule')
# render
ax.plot(amplitude, periode_pendule, color='blue', marker='o')
ax.plot(amplitude, theorie, color='red', marker='o')
ax.legend()
ax.grid()
# sauver png
plt.savefig('graph3.png')
plt.show()