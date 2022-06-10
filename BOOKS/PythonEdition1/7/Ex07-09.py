def calmax(dictdata):
    maxlist = []
    maxdata = max(dictdata.values())
    for data in dictdata:
        if dictdata[data] == maxdata:
            maxlist =[data, maxdata]
    return maxlist

data = {"สงขลา": 500, "พัทลุง": 850, "พัทยา": 650}
ans = calmax(data)
print("ปริมาณน้้ำฝนสูงสุดเท่ากับ", ans[1], "มิลลิเมตร")
print("อยู่ที่จังหวัด"+ ans[0])
