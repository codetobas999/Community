stds_height = [[125, 130, 142, 135, 145],
            [132, 137, 155, 154, 158],
            [150, 154, 155, 153, 160],
            [152, 153, 156, 151, 160],
            [153, 154, 156, 157, 162],
            [155, 156, 154, 160, 162]]

Total_average = 0
Total_year = 0
Average_each_year = []

for i in stds_height:
    sum = 0
    for j in i:
        sum = sum + j
    average = sum / len(i)
    Average_each_year.append(average)
    Total_year = Total_year + 1
    Total_average = Total_average + average

print("Total number of years =",Total_year)
for i in range(0, Total_year):
    print("Student height of year",i+1, "=", Average_each_year[i])
print("Overall of student height = %.2f" %(Total_average/Total_year))
