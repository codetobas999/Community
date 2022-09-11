
ใช้ Docker Desktop เชื่อมกับ Kubernetes บน Google Kubernetes Engine
https://blog.me-idea.in.th/%E0%B9%83%E0%B8%8A%E0%B9%89-docker-desktop-%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%81%E0%B8%B1%E0%B8%9A-kubernetes-%E0%B8%9A%E0%B8%99-google-kubernetes-engine-429412fbbe3f


ลองใช้ Cloud Build สร้าง Docker Image ใน Container Registry
https://blog.me-idea.in.th/%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%83%E0%B8%8A%E0%B9%89-cloud-build-%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-docker-image-%E0%B9%83%E0%B8%99-container-registry-4159cf8c8a04


ทำ API ใส่ Docker image deploy to Google Cloud Run
https://blog.me-idea.in.th/%E0%B8%97%E0%B8%B3-api-%E0%B9%83%E0%B8%AA%E0%B9%88-docker-image-deploy-to-cloud-run-89759cb3e8c8


เตาะแตะไปกับ Docker ตอนที่ 1 Containers (Build, Ship and Run)
https://sysadmin.psu.ac.th/2017/07/21/get-started-with-docker-part-1-containers-build-ship-and-run/



https://www.youtube.com/watch?v=LxHiCZCKwa8

เก็บ Docker Image บน Container Registry Google Cloud
https://bugyourdream.com/blogs/2020/4/1/docker-image-on-google-cloud/

### Cloud RUN & Container Registry
## Running core commands
1. List accounts whose credentials are stored on the local system:
    '''
        gcloud config list
    '''

2. List the properties in your active gcloud CLI configuration:
    '''
        gcloud config list
    '''

3. View information about your gcloud CLI installation and the active configuration:
    '''
        gcloud info
    '''

4. View information about gcloud commands and other topics:
    '''
        gcloud info
    '''

    For example, to view the help for gcloud compute instances create
    '''
        gcloud help compute instances create
    '''


## Config Docker 
1. Config Docker Cloud  For location : asia.gcr.io
    '''
        gcloud auth configure-docker
    '''
2. Bulid Docker 
    '''
        docker build -t [HOST:asia.gcr.io]/[PROJECT:my-proj-bas]/[DOCKER-IMAGE] .
    '''
    For example
    '''
        docker build -t asia.gcr.io/my-proj-bas/mydjango .
    '''
3. push Docker
    '''
        docker push [HOST:asia.gcr.io]/[PROJECT:my-proj-bas]/[DOCKER-IMAGE]
    '''
    For example
    '''
        docker push asia.gcr.io/my-proj-bas/mydjango
    '''

gcloud run deploy mydjango --image asia.gcr.io/my-proj-bas/mydjango --platform managed --region=asia-southeast1 --allow-unauthenticated