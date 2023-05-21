
   ## ----------------------------------------THIS IS 'FIREBASE' ------------------------------------------------------##
 ## -------------------------- Using Firebase Authentication and Realtime Database   -----------------------------------##
## -------------------------- This will be called everywhere data needs to be validated-----------------------------------##

## ______________________________________________________________________________________________________________________##

import pyrebase # Python wrapper for the Firebase API aka Firebase library for Python
import requests
## ______________________________________________________________________________________________________________________##

# Initiallising Firebase
def firebase_config():
    firebaseConfig = {
        'apiKey': "AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME",
        'authDomain': "family-area-network.firebaseapp.com",
        'databaseURL': "https://family-area-network-default-rtdb.asia-southeast1.firebasedatabase.app",
        'projectId': "family-area-network",
        'storageBucket': "family-area-network.appspot.com",
        'messagingSenderId': "601603660956",
        'appId': "1:601603660956:web:844e256757af50cc2be159",
        'measurementId': "G-JTL2XV1WG8",
        'serviceAccount':'C:/Users/Nina/Downloads/family-area-network-firebase-adminsdk-okm5h-03059d1245.json'
    }
    firebase = pyrebase.initialize_app(firebaseConfig)   
    
    return firebase  

# Initiallising Firebase authentication

def firebase_auth():
    firebase=firebase_config() 
    auth=firebase.auth()
    return auth

# Initiallising Firebase Database
def firebase_database():
    firebase=firebase_config() 
    database=firebase.database()
    return database

# will be the logout function
def firebase_out():
    firebase=firebase_config() 
    
    

