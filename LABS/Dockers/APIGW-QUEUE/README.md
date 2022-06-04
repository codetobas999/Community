
![Plugin-rate-limiting](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/APIGW-QUEUE/images/API_GW_new-ServiceDiagram.jpg)
# ขั้นตอนการ Run 
1. เตรียมค่าต่างๆ
    ```command
        Create hosts(C:\Windows\System32\drivers\etc\hosts)
        127.0.0.1 kong.dev.docker
        127.0.0.1 konga.dev.docker
    ```
3. สร้าง Docker network ที่ใช้งาน
    ```docker
       docker network create proxy_network
       docker network create kong_network
       docker network create queue_network
    ```
4. ReverseProxy : xxxx
    ```command
      cd NginxReverseProxy
      docker-compose up -d
    ```
5. KongServer : xxxx
   ```command
      cd KongAPIGW
      docker-compose up -d
    ```
     - [x] #Konga Admin : http://konga.dev.docker(admin/S@msak8192)
        - Create User Admin (Name : Devops , Kong Admin URL : http://kong:8001)
        - Create Service (Service Name, Protocol, Host (Private IP Address), Port และ Path)
     - [x] #(Service Name : registerQueueGW, Protocol : http , Host : 192.168.1.136  , Port : 9001 , Path : /registerqueue)
       - Create Route (Route Name ใส่ข้อมูล Paths, Methods และ Protocols)
     - [x] #(Route Name : registerQueueRoute , Paths : /registerqueue , Methods : POST , Protocols : http)

6. RabbitMQServer : xxxx
   ```command
      cd RabbitMQServer
      docker-compose up -d
    ```
      - [x] #RabbitMQ Admin : localhost:15672 (guest/guest)
7. Producer : xxxx
   ```command
      cd RabbitMQProducer
      docker-compose up -d
   ```
      - [x] #Test For Postman : http://kong.dev.docker/registerqueue 
      - [x] #Check Queue in RabbitMQServer จะต้องมี Queue เข้าไปรอ
8. Consumer : xxxx
    ```command
      cd RabbitMQConsumer
      docker-compose up -d
    ```
      - [x] #Test For Postman : http://kong.dev.docker/registerqueue 
      - [x] #Check Queue in RabbitMQServer จะต้องมีการเอาข้อมูลใน Queue ไปยิง API
      - [x] #ตรวจสอบ Log in Mockoon
8. Kong-Service : xxxx   
        <table>
        <tr>
            <td>No</td>
            <td>Name</td>
            <td>URL</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Mockoon-GW</td>
            <td>http://192.168.1.136:3000/</td>
        </tr>
        <tr>
            <td>2</td>
            <td>registerQueueGW-Container</td>
            <td>http://192.168.1.136:9001/registerqueue</td>
        </tr>  
        </table>  
7. Kong-Route : xxxx   
        <table>
        <tr>
            <td>No</td>
            <td>Name</td>
            <td>Paths</td>
            <td>Headers</td>
            <td>Methods</td>
            <td>Protocols</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Group-1-Route</td>
            <td>/queryPayment  , /confirmPayment</td>
            <td>project-code:MPAY/</td>
            <td>POST</td>
            <td>http</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Group-2-Route</td>
            <td>/queryPayment  , /confirmPayment , /queryDocument</td>
            <td>project-code:USSD,XUSSD/</td>
            <td>POST</td>
            <td>http</td>
        </tr>    
        <tr>
            <td>3</td>
            <td>registerQueueRoute-A</td>
            <td>/registerqueue</td>
            <td>project-code:USSD,XUSSD/</td>
            <td>POST</td>
            <td>http</td>
        </tr>   
        </table> 
  12. Kong-Plugin
      - Authen
      - Rate Limit
            ![Plugin-rate-limiting](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/APIGW-QUEUE/images/Plugin-rate-limiting.png)
        
      - Request Transform : Script Lua Script // แก้ไข Project-code และ X-original-uri
            ![Plugin-request-transformer.png](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/APIGW-QUEUE/images/Plugin-request-transformer.png)
      ```
      GROUP:$((function()
        local pjcode = headers["Project-code"]
        local xpath = headers["X-original-uri"]
        if pjcode == "USSD" or pjcode == "XUSSD" then
          if xpath == "/queryPayment" then
            return "G1"
          elseif xpath == "/queryDocument" then
            return "G2"  
          elseif xpath == "/confirmPayment" then
            return "E1"
          else
            return "ER"  
          end                  
        else
          return "ER99"    
        end  
        end)())
      ```
# ขั้นตอนการทดสอบ
1. ทดสอบผ่าน Postman
        <table>
        <tr>
            <td>No</td>
            <td>Methods</td>
            <td>URL</td>
            <td>Authen</td>
            <td>Header</td>
            <td>Body</td>
            <td>Remark</td>
        </tr>
        <tr>
            <td>1</td>
            <td>GET</td>
            <td>http://kong.dev.docker/registerqueue</td>
            <td>Basic Auth : demo/demo</td>
            <td>project-code:MPAY|USSD|XUSSD</td>
            <td>{
                 "param_queue_name": "queue",
                 "param_exchange_name": "",
                 "param_routing_key_name": "hello",
                 "service_method": "GET",
                 "service_url": "http://192.168.1.136:3000/mockGET",
                 "service_input": "",
                 "service_sleep": 2
                }</td>
            <td>เพื่อไว้ทดสอบดูเรื่อง Queue Process</td> 
        </tr>
        <tr>
            <td>2</td>
            <td>POST</td>
            <td>http://kong.dev.docker/registerqueue</td>
            <td>Basic Auth : demo/demo</td>
            <td>project-code:MPAY|USSD|XUSSD</td>
            <td>{
             "param_queue_name": "queue",
             "param_exchange_name": "",
             "param_routing_key_name": "hello",
             "service_method": "POST",
             "service_url": "http://192.168.1.136:3000/mockPOST",
             "service_input": "{''name'': ''Alice'', ''age'': 31, ''children''}",
             "service_sleep": 2
            }</td>
            <td>เพื่อไว้ทดสอบดูเรื่อง Queue Process</td> 
        </tr>  
        <tr>
            <td>3</td>
            <td>POST</td>
            <td>http://kong.dev.docker/queryPayment</td>
            <td>Basic Auth : demo/demo</td>
            <td>project-code:MPAY|USSD|XUSSD</td>
            <td>{}</td>
            <td>เพื่อไว้ทดสอบดูเรื่อง Rate Limit</td> 
        </tr>   
        <tr>
            <td>4</td>
            <td>POST</td>
            <td>http://kong.dev.docker/confirmPayment</td>
            <td>Basic Auth : demo/demo</td>
            <td>project-code:MPAY|USSD|XUSSD</td>
            <td>{}</td>
            <td>เพื่อไว้ทดสอบดูเรื่อง Rate Limit</td>  
        </tr>   
        <tr>
            <td>5</td>
            <td>POST</td>
            <td>http://kong.dev.docker/queryDocument</td>
            <td>Basic Auth : demo/demo</td>
            <td>project-code:MPAY|USSD|XUSSD</td>
            <td>{}</td>
            <td>เพื่อไว้ทดสอบดูเรื่อง Rate Limit</td>  
        </tr>   
        </table> 
