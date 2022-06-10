import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rc("font", family="TH Krub", size=18)

labels = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน"]
data1 = np.array([20, 25, 25, 26, 55, 38])
data2 = np.array([23, 22, 55, 36, 25, 23])
data = [data1, data2]

fig, ax = plt.subplots()
ax.bar(labels, data1, 0.30, label='2562', color='red')
ax.bar(labels, data2, 0.30, bottom=data1, label='2563', color='blue')
ax.legend()
ax.set_title('ปริมาณน้ำฝนเดือนมกราคม - มิถุนายน เปรียบเทียบระหว่าง ปี พ.ศ. 2562 และ 2563')
ax.set_xticks([])
ax.set_xlabel("")
ax.set_ylabel('ปริมาณน้ำฝน (มม.)')
ax.table(cellText=data, rowLabels=['2562', '2563'], colLabels=labels, loc='bottom')

plt.show()

