passList = {"236428": "sci", "339212": "nurse", "326224": "sci", "818339": "engineer", "111212": "nurse"}
facList =  {"sci": "วิทยาศาสตร์", "nurse": "พยาบาลศาสตร์", "engineer": "วิศวกรรมศาสตร์"}
studentID = input("ป้อนข้อมูลเลขที่ผู้สมัคร >>> ")
if studentID in passList:
    facCode = passList.get(studentID)
    print("คุณสอบได้คณะ", facList[facCode])
else:
    print("คุณสอบไม่ผ่าน เจอกันใหม่รอบหน้า")
