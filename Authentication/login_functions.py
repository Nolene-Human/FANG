
import streamlit as lit
import launch_pages

import Firebase.firebaseconfig
import registered_pages.zero_trust

def user_login():

        auth= Firebase.firebaseconfig.firebase_auth()
        email = lit.sidebar.text_input("Please enter your registered email")
        password = lit.sidebar.text_input("Please enter your password",type='password')

        login=lit.sidebar.checkbox("Login")
                         
        if login:
            database=Firebase.firebaseconfig.firebase_database()

            user=auth.sign_in_with_email_and_password(email,password)
            registered_pages.zero_trust.dashboard()
            name=database.child(user['localId']).child('AccountName').get().val()
            lit.sidebar.markdown("---------------------------")
            lit.sidebar.subheader("Hi " + name)
            lit.sidebar.markdown("---------------------------")
            
        
        else:
            launch_pages.launch.launch()


#       lit.error(" This looks phishy? Are you attempting a Dictionary Attack? Cause we limit your attempts to three tries, sheer brute force won't work.",icon="🤖")
#       lit.write("But users are human so if you forgot your password press reset to go through the authentication process")