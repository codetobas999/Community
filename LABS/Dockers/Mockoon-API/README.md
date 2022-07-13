
# ขั้นตอนการ Run Mockoon ผ่าน Docker

## 1. เตรียมไฟล์ data.json มีขั้นตอนดังนี้
     
   1. เข้า Progran Mockoon และทำการ export file json
     ![export-json-1.jpg](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/Mockoon-API/images/export-json-1.jpg)
     
   2. นำไฟล์ data.json ไปวางไว้ใน folder 
   
          D:\Forks\github\codetobas999\Community\LABS\Dockers\Mockoon-API\mockup-data

## 2. Run Docker เพื่อเริ่มทำงาน Mockup API มีขั้นตอนดังนี้

   1. Run Command
          
          docker run -d --mount type=bind,source=D:\Forks\github\codetobas999\Community\LABS\Dockers\Mockoon-API\mockup-data\data.json,target=/data,readonly -p 3000:3000 mockoon/cli:latest -d data -p 3000
        
        *** D:\Forks\github\codetobas999\Community\LABS\Dockers\Mockoon-API\mockup-data\data.json ต้องใส่ Path ตาม Step 1   
        *** ชือทั้ง 3 จุดจะต้องเหมือนกัน 
       ![export-json-2.jpg](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/Mockoon-API/images/export-json-2.jpg)
  3. Test Mockup
          
          http://localhost:3000/mockGET


## 3. [Documentation](https://mockoon.com/docs/latest/about/)
