import random
import pyrebase

config = {
    "apiKey": "AIzaSyArHZXQ9wiJNOPkhvV18QJJLDVQa1juC-s",
    "authDomain": "scrapping-9c4c2.firebaseapp.com",
    "databaseURL": "https://scrapping-9c4c2.firebaseio.com",
    "projectId": "scrapping-9c4c2",
    "storageBucket": "scrapping-9c4c2.appspot.com",
    "messagingSenderId": "232512095653",
    "appId": "1:232512095653:web:2180911702dbc68dbd944c",
    "measurementId": "G-4LZS8CR2TY"}


firebase = pyrebase.initialize_app(config)
database=firebase.database()
storage = firebase.storage()

def loadfile(filename):
    storage.child("cocooooo/"+filename).download(filename)
def savefile(filename):
    storage.child("cocooooo/"+filename).put(filename)
def getrandomid(n=8):
    A="AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn0123456789"
    m=len(A)
    s=""
    for i in range(n):
        r=random.randint(0,m-1)
        s+=A[r]
    return s

def upload(jsondatastring,type="json"):
	a=getrandomid()#str(random.randint(1,19999))
	database.child("data/%s/"%(type)+a).set(jsondatastring)
	return a


def uploadimage(imagename):
    a=getrandomid()#str(random.randint(1,19999))
    storage.child("images/%s.svg"%(a)).put(imagename)
    return storage.child("images/%s.svg"%(a)).get_url("hhh")


def uploadfilds(st,a):
    database.child("data/json/"+a).set(st)
