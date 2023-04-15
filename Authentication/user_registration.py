import streamlit as lit


#authentication
import Firebase.firebaseconfig
import launch_pages.launch


def register():
    
    launch_pages.launch.launch()

    firebase=Firebase.firebaseconfig.firebase_config()
    database=firebase.database()
    auth = firebase.auth()
    
    #storage=firebase.storage()

    lit.sidebar.subheader("Lets get Registered")
     
    email=lit.sidebar.text_input("Your Email address")
    password=lit.sidebar.text_input("Enter your password",type="password")
    confirmpass=lit.sidebar.text_input("Confirm password",type="password")

    submitted =lit.sidebar.checkbox("Register")
    
           
    if submitted:
            if password !=confirmpass:
                lit.sidebar.warning("Your passwords did not match please try again") 
                
            else:
                user=auth.create_user_with_email_and_password(email,password)
                lit.sidebar.success("Your Account has been created")
                database.child(user['localId']).child("ID").set(user['localId'])   
                lit.sidebar.write("You can now login to your account to get started.")

