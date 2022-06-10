dic = {"10110":"เขตคลองเตย", "50000":"อำเภอเมืองเชียงใหม่", "21000":"อำเภอเมืองระยอง", "40000":"อำเภอเมืองขอนแก่น", "83000":"อำเภอเมืองภูเก็ต"}
amphor = input("Enter your the code of amphor that would like to find :")
while amphor != "exit":
    if dic[amphor]:
        print("Name of this code is ", dic[amphor])
    else:
        print("This code is not in the database")
print("Good bye...")
