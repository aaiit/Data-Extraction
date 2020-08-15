import pyrebase

config = {
  "apiKey": "AIzaSyCH8SXOJOx8X5iinIwH6397pVsCjsks73g",
  "authDomain": "great-cnc.firebaseapp.com",
  "databaseURL": "https://great-cnc.firebaseio.com",
  "projectId": "great-cnc",
  "storageBucket": "great-cnc.appspot.com",
  "messagingSenderId": "899527912747",
  "appId": "1:899527912747:web:0220201b8c6a231a2ea96e",
  "measurementId": "G-K6KDBTM9T7"
}
firebase = pyrebase.initialize_app(config)
storage=firebase.storage()

def getUrlOfZip(path):
	storage.child(path).put(path)
	return storage.child(path).get_url("hh")

