
# ขั้นตอนการ Run Mockoon ผ่าน Docker
##1. เตรียมไฟล์ data.json 
     มีขั้นตอนดังนี้
     1. เข้า Progran Mockoon และทำการ export file json
     ![export-json-1.jpg](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/Mockoon-API/images/export-json-1.jpg)
     2. นำไฟล์ data.json ไปวางไว้ใน folder : 
    ```command
        D:\Forks\github\codetobas999\Community\LABS\Dockers\Mockoon-API\mockup-data
    ```

##2. Run Docker เพื่อเริ่มทำงาน Mockup API
    1. เข้า cmd และไปที่ D:\Forks\github\codetobas999\Community\LABS\Dockers\Mockoon-API\mockup-data
    ```command
        cd D:\Forks\github\codetobas999\Community\LABS\Dockers\Mockoon-API\mockup-data
        d:
    ```
    2. Run Command
    ```docker
       docker run -d --mount type=bind,source=d:/mocks/data.json,target=/data,readonly -p 3000:3000 mockoon/cli:latest -d data -p 3000
    ```
    3. Test Mockup
    ```html
       http://localhost:3000/users
    ```
