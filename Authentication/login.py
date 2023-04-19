
   ## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Tick box in this area is not ideal
# - Form does not reset or hides when user logs in

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit


## ______________________________________________________________________________________________________________________##

import launch_pages # Import applications Launch page function

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication Function
import registered_pages.zero_trust # if successfull navigate user to the zero_trust landing page -> User Dashboard


## ______________________________________________________________________________________________________________________##
def login():

        # Calling Firbase Config Authentication Function
        auth= Firebase.firebaseconfig.firebase_auth()
        
        # Form / User Input
        email = lit.sidebar.text_input("Please enter your registered email")
        password = lit.sidebar.text_input("Please enter your password",type='password')

        login=lit.sidebar.checkbox("Login")

         # Rules and Checks once user press the 'login' button              
        if login:
                        
             user=auth.sign_in_with_email_and_password(email,password) # Authenticates registered users agains password
             registered_pages.zero_trust.dashboard() # Once Authenticated then the users dashboard with user details are displayed   
            
             # Database Get function to display Welcome message in Sidebar
             database=Firebase.firebaseconfig.firebase_database()
             name=database.child(user['localId']).child('AccountName').get().val()
             lit.sidebar.markdown("---------------------------")
             lit.sidebar.subheader("Hi " + name)
             lit.sidebar.markdown("---------------------------")
             
         # If user is not validated then the user can only see the Launch Page
        else:
             launch_pages.launch.launch()

#       lit.error(" This looks phishy? Are you attempting a Dictionary Attack? Cause we limit your attempts to three tries, sheer brute force won't work.",icon="🤖")
#       lit.write("But users are human so if you forgot your password press reset to go through the authentication process")
        

                    