import streamlit as lit


#authentication
import pyrebase
import Firebase.firebaseconfig

firebase=Firebase.firebaseconfig.firebase_config()
      
auth = firebase.auth()
database=firebase.database()
#storage=firebase.storage()


lit.write("This is the registration page")
FAN_name=lit.text_input("Give your Network a name: ",value="my_home_network")
            
email=lit.text_input("Your Email address")
password=lit.text_input("Enter your password: ",type="password")
confirmpass=lit.text_input("Confirm password: ",type="password")

submitted =lit.button("Register")
            
if submitted:
    user = auth.create_user_with_email_and_password(email,password)
    lit.success("Your Account has been created")
    user=auth.sign_in_with_email_and_password(email,password)
    database.child(user['localId']).child("Handle").set(FAN_name)
    database.child(user['localId']).child("ID").set(user['localId'])
    lit.tiltle("FANG welcomes , "+ FAN_name)
    lit.write("You can now login to your account to get started.")



                              
                    


