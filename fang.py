## ----------------------------------------THIS IS 'MAIN' ----------------------------------------------- ##
## ----------Launced when application start and is the only 'page' in this application------------------##
## --------All other 'pages' are called functions displayed when conditions have been met-------------##

# - NO FUTURE DEVELOPMENT PLANNED - #

## ______________________________________________________________________________________________________________________##

## Importing Front-end tool Streamlit (https://streamlit.io/)
import streamlit as lit
from PIL import Image #used to display images on page

## ______________________________________________________________________________________________________________________##

## Import applications Login and Registration Functions ##
import launch_pages.launch
import Authentication.user_registration
import Authentication.user_login
import Firebase.firebaseconfig
import Authentication.mfa
import Security.remove_QR

import Authentication.loginform 
import requests

#animation
import json
from streamlit_lottie import st_lottie


import pyotp
import qrcode
import time

auth= Firebase.firebaseconfig.firebase_auth()
database=Firebase.firebaseconfig.firebase_database()


## ______________________________________________________________________________________________________________________##


## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##
   

## Side Bar and Navigation
home=lit.sidebar.radio("""**WELCOME**""",['Home','Register','Login',"Reset Password"],key="visible")

## ______________________________________________________________________________________________________________________##

if home == 'Login':  

        emailcol, passwordcol = lit.columns(2)
        email = emailcol.text_input("Please enter your registered email")
        password = passwordcol.text_input("Please enter your password",type='password')
        
        try:
                user=auth.sign_in_with_email_and_password(email,password)
                mfa_check=database.child(user['localId']).child("mfa").get().val()
                
                if mfa_check==0:
                        emailcol.warning("FANG uses time-based one-time passcodes (TOTP) that are compliant with all major authenticator apps and browser extensions including 1Password, Authy, and Google Authenticator.")
                        new_OTP=database.child(user['localId']).child("Userkey").get().val()
                        generated_OTP=Authentication.mfa.generatepin(new_OTP)
                        passwordcol.write("**Open or Download your favourite Authentication app**")
                        passwordcol.write("**Add account by scanning QR code**")
                        uri=pyotp.totp.TOTP(new_OTP).provisioning_uri(name="FANG",issuer_name="FANG App")
                        qrcode.make(uri).save("QR.png")
                        emailcol.image("QR.png",width=150)

                        first_verify=passwordcol.text_input("Verify Code, press enter")

                        if first_verify == generated_OTP:
                                emailcol.success("Great you are now registered")
                                database.child(user['localId']).update({"mfa":1})
                                emailcol.header("You are logged in!")
                                emailcol.write("Thank you for testing ")
                                with lit.spinner('We are deleting your QR code for security reasons'):
                                        time.sleep(5)
                                        Security.remove_QR.del_QR()
                                lit.success('Done!')
        

                        else:
                                lit.write("codes dont match")

                if mfa_check==1:
                                lit.sidebar.markdown("---") 
                                new_OTP=database.child(user['localId']).child("Userkey").get().val()
                                generated_OTP=Authentication.mfa.generatepin(new_OTP)

                                user_mfa=lit.sidebar.text_input("Enter verification Code")
                                yourmfa = lit.sidebar.button(":flying_saucer: Let's Go ")
                                                
                                lit.sidebar.markdown("---")

                                if user_mfa == generated_OTP:
                                        lit.success("You are logged in!")
                                        lit.write("Thank you for testing ")


                                else:
                                        lit.sidebar.error("**Code not valid**")               
                        
        except requests.exceptions.HTTPError as err:
                lit.markdown("*Please enter valid info*") 

        

elif home=="Reset Password":
                launch_pages.launch.launch()
                email=lit.sidebar.text_input("Please enter your email address")
                reset_pass=lit.sidebar.button("Reset password")

                if reset_pass:
                        reset=Firebase.firebaseconfig.firebase_auth()
                        reset.send_password_reset_email(email, action_code_settings=None)
                        lit.sidebar.write("Reset Password email has been sent") 
                        

elif home == 'Register':
        Authentication.user_registration.register()


else:
      launch_pages.launch.launch()  

        