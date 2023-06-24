
   ## ----------------------------------------THIS IS 'FIREBASE' ------------------------------------------------------##
 ## -------------------------- Using Firebase Authentication and Realtime Database   -----------------------------------##
## -------------------------- This will be called everywhere data needs to be validated-----------------------------------##

## ______________________________________________________________________________________________________________________##


## ______________________________________________________________________________________________________________________##



import pyrebase # Python wrapper for the Firebase API aka Firebase library for Python
def firebase_config():
    firebaseConfig = {
        'apiKey': "AIzaSyBCedGxRpePNJ9Dq48U07w2hAH2oS4Ey-g",
        'authDomain': "fang-407da.firebaseapp.com",
        'databaseURL': "https://fang-407da-default-rtdb.asia-southeast1.firebasedatabase.app",
        'projectId': "fang-407da",
        'storageBucket': "fang-407da.appspot.com",
        'messagingSenderId': "412571808822",
        'appId': "1:412571808822:web:6ad6b4268828f4a1661497",
        'measurementId': "G-498TCQ81KF"
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
