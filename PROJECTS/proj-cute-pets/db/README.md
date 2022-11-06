# fcc-fastapi-jwt
This project holds the code for explanatory article published on freecodecamp.

If you want to learn full implementation of user authentication with fastapi, while creating a full fledge backend, here is the video version.

[https://www.youtube.com/watch?v=G8MsHbCzyZ4&ab_channel=ABDLogs](https://www.youtube.com/watch?v=G8MsHbCzyZ4)

## Forking project on replit
You can run/fork this project on replit here --> https://replit.com/@abdadeel/FastAPI-Starter


## Setting up locally

To setup the project locally clone the repository.

```shell
git clone https://github.com/mabdullahadeel/fcc-fastapi-jwt
```

Install required dependencies.

```shell
pip install -r requirements.txt
```

To run the server in development mode

```shell
python runserver.py
```

```step
cd D:\Forks\github\Community\PROJECTS\proj-cute-pets\backend
python -m venv venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install fastapi "uvicorn[standard]" beanie python-decouple email-validator python-jose[cryptography] python-jose[cryptography] "passlib[bcrypt]" python-multipart  
pip install -r requirements.txt
pip freeze > requirements.txt
deactivate

--Run App
uvicorn app.app:app --reload
 
--Init
1. Start MongoDB On Docker Compose(D:\Forks\github\Community\PROJECTS\proj-cute-pets\db)

```

```Concep
API/AUTH/JWT       -->Service(UserService) --> Model(schema) --> DB
API/API_V1/Handles --> Service --> Model(schema) --> DB
```

