import pandas as pd
import matplotlib.pyplot as plt


filename = "coursedata2.csv"
cols = ['id', 'major', 'gender', 'subject', 'category', 'grade', 'year', 'total']
data = pd.read_csv(filename, usecols=cols, encoding='utf-8')
df = data.pivot_table(index=['category'], columns=['major'], values=['total'], aggfunc='count')
ax = df.plot.line(rot=0, title="TOTAL STUDENT OF SUBJECT CATEGORY BY MAJOR", ylabel="total student", table=True)
ax.set_xticks([])
ax.set_xlabel("")

for col in df.columns:
    for i, val in enumerate(df[col]):
        ax.text(i, val, str(val))
plt.show()
