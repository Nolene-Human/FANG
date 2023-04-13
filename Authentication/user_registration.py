import streamlit as lit


#authentication
import pyrebase
import Firebase.firebaseconfig
import launch_pages.launch


def register():
    
    launch_pages.launch.launch()

    firebase=Firebase.firebaseconfig.firebase_config()
        
    auth = firebase.auth()
    database=firebase.database()
    #storage=firebase.storage()


    lit.sidebar.write("Lets get Registered")
    FAN_name=lit.sidebar.text_input("Give your Network a name: ")
                
    email=lit.sidebar.text_input("Your Email address")
    password=lit.sidebar.text_input("Enter your password: ",type="password")
    confirmpass=lit.sidebar.text_input("Confirm password: ",type="password")

    
    submitted =lit.sidebar.button("Register")

           
    if submitted:
            if password !=confirmpass:
                lit.sidebar.warning("Your passwords did not match please try again") 
            
            else:
                user = auth.create_user_with_email_and_password(email,password)
                lit.sidebar.success("Your Account has been created")
                
                
                #add to database
                user=auth.sign_in_with_email_and_password(email,password)
                database.child(user['localId']).child("Handle").set(FAN_name)
                database.child(user['localId']).child("ID").set(user['localId'])
                lit.sidebar.write("FANG welcomes , "+ FAN_name)
                lit.sidebar.write("You can now login to your account to get started.")

