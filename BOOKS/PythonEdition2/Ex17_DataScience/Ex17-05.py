import decimal as dm
import pandas as pd
import matplotlib.pyplot as plt


filename = "coursedata2.csv"
cols = ['id', 'major', 'gender', 'subject', 'category', 'grade', 'year', 'total']
data = pd.read_csv(filename, usecols=cols, encoding='utf-8')
df = data.pivot_table(index=['category'], columns=['gender'], values=['grade'], aggfunc='mean')
ax = df.plot.bar(width=0.3, rot=0, title="AVERAGE GRADE OF SUBJECT CATEGORY BY GENDER", ylabel="Average of Grade")
ax.set_xlabel("Category of Subject")
for p in ax.patches:
    x = p.get_x() + 0.005
    y = p.get_height() + 0.005
    ax.annotate('{:.2f}'.format(dm.Decimal(str(p.get_height()))), (x, y), fontsize=10)
plt.show()
