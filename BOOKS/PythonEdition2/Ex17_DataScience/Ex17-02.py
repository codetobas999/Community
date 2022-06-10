import pandas as pd


filename = "coursedata1.csv"
cols = ['id', 'major', 'gender', 'subject', 'category', 'grade', 'year', 'total']
data = pd.read_csv(filename, usecols=cols, encoding='utf-8')
totalrow = data.shape[0]
print("filename : ", filename)
print("****", totalrow, "records imported ****")
print("*******************************************")
print("the duplicated records")
dup_data = data[data.duplicated()]
print(dup_data['id'])
print("*******************************************")
data.drop_duplicates(inplace=True)
totalrow = data.shape[0]
print("duplicated records are deleted")
print("*******", totalrow, "records left *******")

miss_data = 'subject'
m = data[miss_data].mode()
data[miss_data] = data[miss_data].fillna(m[0])

filename = "coursedata2.csv"
data.to_csv(filename)
