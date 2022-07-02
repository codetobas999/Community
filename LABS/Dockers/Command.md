# Command Docker

# Push to Docker

   - Login Docker 
      ```
      docker login -u [user]    
      ```
      Examle : docker login -u ballketball999
   - ทำ tag Image
      ```
      docker tag [Image Name] ballketball999/[Image Name(ตัวเล็กทั้งหมด)]:[Version]      
      ```
      Examle : docker tag rabbitmqproducer_producer ballketball999/rabbitmqproducer:1.0
   - Push Image to Docker hub
      ```
      docker push ballketball999/[Image Name(ตัวเล็กทั้งหมด)]:[Version]
      ```
      Examle : docker push ballketball999/rabbitmqproducer:1.0 

# Command Docker
  ![Plugin-rate-limiting](https://github.com/codetobas999/Community/blob/main/LABS/Dockers/images/docker-lifecycle.png)
  - Docker build Image
      ```
      docker build -t [tag]    
      ```
      Examle : docker build -t demo-image:1.0
  - Docker save Image : Save Image in docker host
      ```
      docker save -o [file_image_Name].tar [image Name]   
      ```
      Examle : docker save -o demo-image.tar demo-image
  - Docker load Image : Load Image from docker host
      ```
      docker load -i [file_image_Name].tar  
      ```
      Examle : docker load -i demo-image.tar 
  - Docker load commit : Save Container to Image
      ```
      docker commit [container_id] [image_name] 
      ```
      Examle : docker [container_id] demo-image
  - Docker run Image : Run Image
      ```
      docker run xxx
      ```
      Examle : docker run xxx
  - Docker history Image : Specifies to create a mirror of history 
      ```
      docker history [OPTIONS] [image]
      ```
      Examle : docker history w3big/ubuntu:v3      
  - Docker network Create : Create Network on Docker
  - Docker network Connect : Connect Container to Network on Docker
  - Docker log : View Log In Container
      ```
      docker logs [option] [container_id] 
      ```
      Examle : docker logs xxx 
      
      Examle : docker logs -f xxx | more      
  
# Command Docker-compose
  - Docker Compose Stop : Stop All Container on Docker Compose
      ```
      docker-compose stop
      ```
  - Docker Compose Build : Build All Container on Docker Compose
      ```
      docker-compose build
      ```  
  - Docker Compose Start : Start All Container on Docker Compose
      ```
      docker-compose start
      ```
  - Docker Compose Up : Run All Image on Docker Compose
      ```
      docker-compose up -d
      ``` 
  - Docker Compose Down : Stop All Image on Docker Compose 
      ```
      docker-compose down --rmi all
      ```
  
