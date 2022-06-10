import pandas as pd
import matplotlib.pyplot as plt


filename = "coursedata2.csv"
cols = ['id', 'major', 'gender', 'subject', 'category', 'grade', 'year', 'total']
data = pd.read_csv(filename, usecols=cols, encoding='utf-8')
df = data.pivot_table(index=['category'], values=['total'], aggfunc='count')
my_colors = ["green", "pink", "red", "yellow"]
df.plot.pie(table=True, subplots=True, title="PERCENT OF TOTAL STUDENT FOR EACH SUBJECT CATEGORY",  legend=None, colors=my_colors, autopct='%1.1f%%', radius=1)
plt.show()
