# คําสั่งของ docker

1. docker ls เป็นคําสั่งดูว่าขณะนี้มี  container ตัวไหนรันอยู่บ้าง รูปแบบการใช้คําสั่งคือ
 ```
    docker ls
 ```
2. docker images เป็นคําสั่งดูว่าในเครื่องเรามี Image อะไรอยู่บ้าง หมายถึง image ที่ pull มาอยู่บนเครื่องเราแล้ว วิธีใช้คือ
 ```
    docker images
 ```
3. docker rm เป็นทําสั่งสําหรับลบ container รูปแบบการใช้งานทําสั่งคือ
 ```
    docker rm [ชื่อ หรือid ของ container]
 ```
***จะลบได้เฉพาะ container ที่ stop อยู่เท่านั้น ถ้าต้องการลบ container ที่กําลังรันอยู่ ให้เพิ่ม option -f เข้าไป 4. docker rmi เป็นคําสั่งลบ image ที่อยู่ในเครื่อง รูปแบบคําสั่งคือ
 ```
    docker rmi [ชื่อ หรือid ของ image ที่จะลบ]
 ```
***จะไม่สามารถลบ Image ที่มี container รันอยู่ได้ 5. docker run เป็นคําสั่ง run container รูปแบบการใช้งานคําสั่งคือ
 ```
    docker run [option] [ชื่อ image] [command]
 ```
    [option] คือ option ต่างๆ เช่น -p คือ map port ฯลฯ
    [ชื่อ image] คือ ชื่อของ image ที่เราจะ run
    [connamd] คือ command ที่ต้องการทํา เมื่อ container start แล้ว

ตัวอย่าง
 ```
    docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx
 ```
6. docker start คําสั่ง start container วิธีใช้คือ
 ```
    docker start [ชื่อ container]
 ```
7. docker stop คําสั่ง stop container
 ```
    docker stop [ชื่อ container]
 ```
5. docker stats คําสั่งใช้ดูการใช้ Resource ของแต่ละ Containner (CPU, RAM) รูปแบบการใช้คือ
 ```
    docker stats
 ```
# คําสั่งของ docker compose
 ```
    1. docker-compose ps คําสั่งสําหรับดูว่าขณะนี้มี container ตัวไหนรันอยู่บ้าง (ใน docker-compose ที่เราทํางานอยู่) วิธีใช้คือ
 ```
docker-compose ps

2. docker-compose up คําสั่งสําหรับ start container ทั้งหมดใน docker-compose ที่เราทํางานอยู่ รูปแบบการใช้งานคือ
 ```
    docker-compose up [option]
 ```
ตัวอย่าง ถ้าต้องการรัน conatiner และ build image ด้วย ใช้คําสั่งนี้
 ```
    docker-compose up -d --build
 ```
3. docker-compose down คําสั่ง stop พร้อมทั้งลบ container ด้วย (ใน docker-compose ที่เราทํางานอยู่) รูปแบบคําสั่งคือ
 ```
    docker-compose down
 ```
4. docker-compose stop คําสั่ง stop container ใน docker-compose ที่เราทํางานอยู่ รูปแบบคําสั่งคือ
 ```
    docker-compose stop
 ```
# คําสั่งของ docker swarm 
1. docker swarm init เป็นคําสั่งสําหรับสร้าง docker swarm menager (leader) รูปแบบคําสั่งคือ
 ```
    docker swarm init
 ```
2. docker node ls เป็นคําสั่งสําหรับดู node ทั้งหมดใน swarm วิธีใช้คือ
 ```
    docker node ls
 ```
3. docker node rm เป็นคําสั่งที่ใช้ ลบ node รูปแบบคําสั่งคือ
 ```
    docker node rm [ชื่อ node]
 ```
4. docker swarm join เป็นคําสั่งที่ทําให้เครื่องของเราไป join ใน swarm วิธีใช้คือ
 ```
    docker swarm join [token ได้จาก manager] [ip ของเครื่อง manager]
 ```
5. docker swarm join-token เป็นคําสั่งใช้ get token manager หรือ get token worker เพื่อเป็น token ให้เครื่องอื่นๆมา join ใน swarm รูปแบบคําสั่งคือ
 ```
docker swarm join-token [manager/worker]
 ```
6. docker service create เป็นคําสั่งที่ใช้สร้าง service รูปแบบการใช้คําสั่งคือ
 ```
    docker service [option] [image name] [command]
 ```
    [option] คือ option ต่างๆ เช่น -p คือ map port ฯลฯ
    [image name] คือ ชื่อของ image ที่เราจะ run
    [connamd] คือ command ที่ต้องการทํา เมื่อ service start แล้ว

ตัวอย่าง

docker service create --replicas [จํานวน task ที่ต้องการ] --name [ชื่อ service] -p [port] [image ที่ต้องการ]
 ```
7. docker service ls เป็นคําสั่งสําหรับใช้ดูว่าตอนนี้มี service ตัวไหนรันอยู่บ้าง วิธีใช้คือ
 ```
    docker service ls
 ```
8. docker service ps เป็นคําสั่งดู task ของ service
 ```
    docker service ps [service name]
 ```
9. docker service rm คําสั่งลบ service วิธีใช้คือ
 ```
    docker service rm
 ```
10. docker service scale เป็นคําสั่ง scale task หรือ container
 ```
    docker service scale [ชื่อ service]=[จํานวน task หรือ container ที่ต้องการ]
 ```
11. docker swarm leave คําสั่งเอาเครื่องตัวเอง (เครื่องที่รันคําสั่งนี้) ออกจาก swarm วิธีใช้คือ
 ```
    docker swarm leave
 ```
# เทคนิคการใช้คําสั่ง docker เพิ่มเติม

1. ลบ container ทั้งหมดในคําสั่งเดียว วิธีการลบ container ทั้งหมดภายในคําสั่งเดียวคือ
 ```
    docker rm $(docker pa -a -q)
 ```
2. ลบ image ทั้งหมดในคําสั่งเดียว วิธีการลบ image ทั้งหมดภายในคําสั่งเดียวคือ
 ```
    docker rmi $(docker images -q)
 ```