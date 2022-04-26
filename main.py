from urllib import response
from fastapi import FastAPI
import requests
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List


API_ENDPOINT = "https://development.wpmonitoring.com"
LOGIN_ENDPOINT = API_ENDPOINT + "/api/login/"
CSRF_ENDPOINT = API_ENDPOINT + "/api/csrf/"
SITES_ENDPOINT = API_ENDPOINT + "/api/sites/"
LOG_ENDPOINT = API_ENDPOINT + "/api/security/logs/"
PACKAGE_ENDPOINT = API_ENDPOINT + "/api/packages/"
DASHBOARD_ENDPOINT = API_ENDPOINT + "/api/dashboard/"
REPORTS_ENDPOINT = API_ENDPOINT + "/api/reports/"
SECURITY_ENDPOINT = API_ENDPOINT + "/api/security/"
SETTINGS_ENDPOINT = API_ENDPOINT + "/api/settings/"

# User model
class User(BaseModel):
    email: str
    password: str

# site model
class Site(BaseModel):
    urls: List[str] = []
    package_name: str
    timezone: str

class Setting(BaseModel):
    notification: str
    city: str



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


@app.post("/sites/")
async def sites(user: User):
    
    LOGIN_CREDENTIALS = {
        "email": user.email,
        "password": user.password
    }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(SITES_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/sites/{sites_url}/")
async def sites(user: User, sites_url: str):
    
    LOGIN_CREDENTIALS = {
        "email": user.email,
        "password": user.password
    }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(SITES_ENDPOINT + sites_url + "/", cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/logs/{site_url}/")
async def getSiteLog(user: User, site_url: str):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(LOG_ENDPOINT + site_url + "/", cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/logs/")
async def getSiteLogAll(user: User):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(LOG_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()


@app.post("/packages/")
async def packages(user: User):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    print("package endpoint", PACKAGE_ENDPOINT)
    res = requests.get(PACKAGE_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/dashboard/")
async def dashboard(user: User):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(DASHBOARD_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/reports/")
async def reports(user: User):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(REPORTS_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/reports/{yearmonth}/")
async def reportsMonth(user: User, yearmonth: str):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(REPORTS_ENDPOINT + yearmonth + "/", cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/reports/{site_url}/{yearmonth}/")
async def reportsMonthSite(user: User, site_url: str, yearmonth: str):
    
    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)   
    res = requests.get(REPORTS_ENDPOINT + site_url + "/" + yearmonth + "/", cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/security/")
async def reports(user: User):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(SECURITY_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())

    return res.json()

@app.post("/settings/")
async def reports(user: User):

    LOGIN_CREDENTIALS = {
            "email": user.email,
            "password": user.password
        }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)
    res = requests.get(SETTINGS_ENDPOINT, cookies=res_login.cookies)
    print("response : ", res.json())    

    return res.json()

# Add Sites 
@app.post('/addSite/')
async def addSite(user: User, site: Site):
    LOGIN_CREDENTIALS = {
        "email": user.email,
        "password": user.password
    }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)

    res_csrf = requests.get(CSRF_ENDPOINT)
    print(res_csrf.json())

    response = requests.post(SITES_ENDPOINT, {
        "urls": site.urls,
        "packages_name": site.package_name,
        "timzone": site.timezone
    }, cookies=res_login.cookies)

    print("response : ", response.json())    
    return response.json()


@app.post('/updateSettings/')
async def updateSettings(user: User, setting: Setting):
    LOGIN_CREDENTIALS = {
        "email": user.email,
        "password": user.password
    }

    res_login = requests.post(LOGIN_ENDPOINT, json=LOGIN_CREDENTIALS)
    print("login reponse ", res_login.text)
    print("cookies, ", res_login.cookies)

    response = requests.post(SETTINGS_ENDPOINT, {
        "notification": setting.notification,
        "city": setting.city
    }, res_login.cookies)

    print("response : ", response.json())

