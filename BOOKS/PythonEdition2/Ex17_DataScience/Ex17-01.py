import pandas as pd

fname = "data.csv"
data = pd.read_csv(fname, index_col=0)
totalrow = data.shape[0]
print("filename : ", fname)
print("*******", totalrow, "data records imported *******")
df1 = pd.DataFrame(data[['id', 'sale']])
pd.options.display.float_format = "${:,.2f}".format
print("Data Menu")
print("==================================")
print("1: select data row")
print("2: max-min sale data")
print("3: percent commission grouping data")
print("9: quit")
print("==================================")
while True:
    no = int(input("Enter menu 1, 2 or 3 >>> "))
    if no == 9:
        print("see you")
        break
    if no == 1:
        rowno1 = int(input("Enter row no start >>> "))
        rowno2 = int(input("Enter row no stop >>> "))
        print("=== data records of",  rowno1,  "to" ,  rowno2, "===")
        print(df1[ rowno1-1: rowno2])
        print('==========================')
    if no == 2:
        minsale = df1['sale'].min()
        maxsale = df1['sale'].max()
        print('======== min sale ========')
        df2 = df1.loc[data['sale'] == minsale]
        print(df2)
        print('======== max sale ========')
        df2 = df1.loc[data['sale'] == maxsale]
        print(df2)
        print('========================')
    if no == 3:
        print('======= commission group data ======')
        df3 = pd.DataFrame(data[['percomm', 'sale', 'com']])
        df3 = df3.set_index('percomm')
        df3 = df3.sort_values('percomm')
        grouped_df = df3.groupby('percomm')
        for key, item in grouped_df:
            print("percent commission =", key)
            print("total sale = ${:,.2f}".format(float(grouped_df.get_group(key)['sale'].sum())))
            print("total commission = ${:,.2f}".format(float(grouped_df.get_group(key)['com'].sum())))
        print('===================================')
