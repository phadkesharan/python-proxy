from fastapi import FastAPI
import requests
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


API_ENDPOINT = "https://development.wpmonitoring.com"

LOGIN_ENDPOINT = API_ENDPOINT + "/api/login/"
CSRF_ENDPOINT = API_ENDPOINT + "/api/csrf/"
DATA_ENDPOINT = API_ENDPOINT + "/api/sites/"

class User(BaseModel):
    email: str
    password: str



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"Hello": "World"}

# @app.post("/login/")
# def login():
#     return {"Message": "Test Complete"}


@app.post("/login/")
async def login(user: User):
    
    LOGIN_CREDENTIALS = {
        "email": user.email,
        "password": user.password
    }

    # return {"message": "working"}

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(DATA_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()
