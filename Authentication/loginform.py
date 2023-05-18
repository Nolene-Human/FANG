
import streamlit as lit
import requests

import Firebase.firebaseconfig

def loginform():

    auth= Firebase.firebaseconfig.firebase_auth()
    database=Firebase.firebaseconfig.firebase_database()


    email = lit.sidebar.text_input("Please enter your registered email")
    password = lit.sidebar.text_input("Please enter your password",type='password')
     
    login = lit.sidebar.checkbox("Login")

    if login:
        try:
          user=auth.sign_in_with_email_and_password(email,password) # Authenticates registered users agains password
               
          name=database.child(user["idToken"]).child('AccountName').get().val() #read user data from database and write a greeting  message
          lit.sidebar.subheader("Hi " + name + " Network")
          return user
                   
        except requests.exceptions.HTTPError as err:
          lit.write(err)
          lit.error("There is a problem with the details you entered, please retry.")  
          lit.subheader("""Forgot your password?
              You can reset your password in the drop down list""")  
