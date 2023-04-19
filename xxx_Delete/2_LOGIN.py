import streamlit as lit
from PIL import Image


lit.set_page_config(page_title="LOGIN",
        page_icon="🚀",
        layout="wide")





logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

choice=lit.selectbox("Login or Sign up", ["Login","Sign Up"])

if choice=="Login":
    import Authentication.login
#lit.sidebar.button("Register")
    Authentication.login.user_login()
    lit.sidebar.button("Reset Password")

if choice == "Sign Up":
    import pyrebase

    firebaseConfig = {
        'apiKey': "AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME",
        'authDomain': "family-area-network.firebaseapp.com",
        'databaseURL': "https://family-area-network-default-rtdb.asia-southeast1.firebasedatabase.app",
        'projectId': "family-area-network",
        'storageBucket': "family-area-network.appspot.com",
        'messagingSenderId': "601603660956",
        'appId': "1:601603660956:web:844e256757af50cc2be159",
        'measurementId': "G-JTL2XV1WG8"
    }
        
    firebase = pyrebase.initialize_app(firebaseConfig)       
    auth = firebase.auth()
    database=firebase.database()
    
        #storage=firebase.storage()


    lit.write("Lets get Registered")
    FAN_name=lit.text_input("Give your Network a name: ")
                
    email=lit.text_input("Your Email address")
    password=lit.text_input("Enter your password: ",type="password")
    confirmpass=lit.text_input("Confirm password: ",type="password")

    if password !=confirmpass:
        lit.warning("Your passwords did not match please try again")
    

    get_registered=lit.button("Get Registered")    
    if get_registered:
        user = auth.create_user_with_email_and_password(email,password)
        

        lit.success("Your Account has been created")
        user=auth.sign_in_with_email_and_password(email,password)
        #database.child(user['localId']).child("Handle").set(FAN_name)
        #database.child(user['localId']).child("ID").set(user['localId'])
        lit.title(FAN_name + " Welcome to the Gang")
        lit.write("You can now login to your account to get started.")

        