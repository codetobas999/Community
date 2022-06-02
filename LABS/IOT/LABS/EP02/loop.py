import time

print(list(range(5)))

#for i in [0,1,2,3,4,5]:    #Satrt 0 - 5 (Step 1) 
#for i in range(10):        #Satrt 0 - 9 (Step 1)
#for i in range(2, 6):      #Satrt 2 - 5 (Step 1)
#for i in range(2, 10, 3):  #Satrt 2,5,8 (Step 3)
for i in range(6):          #Satrt 0 - 5 (Step 1)
    if i % 2 == 0 :
        print('ไฟกำลังเปิด : ' + str(i) )
    else :
        print('ไฟกำลังปิด : ' + str(i) )
    time.sleep(2)


for i in ['A','B','C']:    #Satrt A,B,C (Step 1)
    print('Data : ' + str(i) )
