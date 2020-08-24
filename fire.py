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

def upload(jsondatastring):
	a=str(random.randint(1,19999))
	database.child("data/json/"+a).set(jsondatastring)
	return a