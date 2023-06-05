
   ## ----------------------------------------THIS IS 'FIREBASE' ------------------------------------------------------##
 ## -------------------------- Using Firebase Authentication and Realtime Database   -----------------------------------##
## -------------------------- This will be called everywhere data needs to be validated-----------------------------------##

## ______________________________________________________________________________________________________________________##


## ______________________________________________________________________________________________________________________##



import pyrebase # Python wrapper for the Firebase API aka Firebase library for Python
def firebase_config():
    firebaseConfig = {
        'apiKey': "AIzaSyC8o6At1beDcB8HstCbG7pLf6UoPG7UujE",
        'authDomain': "fang1-2befc.firebaseapp.com",
        'databaseURL': "https://fang1-2befc-default-rtdb.asia-southeast1.firebasedatabase.app",
        'projectId': "fang1-2befc",
        'storageBucket': "fang1-2befc.appspot.com",
        'messagingSenderId': "590003298320",
        'appId': "1:590003298320:web:3cdadf5f6f3f05bc5a6a95",
        'measurementId': "G-9LE32FE2KL",
        'serviceAccount':'C:/Users/Nina/Desktop/Phased_Fang/key/fang1-2befc-firebase-adminsdk-wdhnk-c29fe8aaf8.json'
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

import firebase_admin
from firebase_admin import credentials

def admin():
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    admincred=firebase_admin.initialize_app(cred)
    return admincred


# Authenticate Firebase Database, Storage and Auth, programmatically via the unified Admin SDK
import firebase_admin
from firebase_admin import credentials

def firebase_admin():
    cred = credentials.Certificate={'serviceAccount':"C:/Users/Nina/Desktop/Phased_Fang/key/fang1-2befc-firebase-adminsdk-wdhnk-c29fe8aaf8.json"}
    admin_cred=pyrebase.firebase_admin.initialize_app(cred)
    return admin_cred
