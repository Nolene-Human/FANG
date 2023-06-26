
## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - no future developments
## ______________________________________________________________________________________________________________________##

import streamlit as lit
import time
import pyotp
import random
## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase SDK's
import Authentication.mfa #otp functions
import Security.remove_QR
## ______________________________________________________________________________________________________________________##

database=Firebase.firebaseconfig.firebase_database()
auth= Firebase.firebaseconfig.firebase_auth()
## ______________________________________________________________________________________________________________________##

this_user_detail=[]
this_user_id=[]

def login_form():

    lit.subheader("Login")

    email=lit.text_input("Your Email address")
    password=lit.text_input("Confirm password",type="password")
    
    lit.subheader("Verification")
    user_OTP=lit.text_input("Please enter OTP Code",type="password")
              
    if email == "" or password=="" or user_OTP=="":
        lit.warning("Please enter all fields")

    try:           
        if email != "" and password!="" or user_OTP!="":
            login={'email':email,'password':password,'opt':user_OTP}
            this_user_detail.append(login)    
    except:
          #this_user_detail.clear()
          lit.write('Welcome back')
           
           
            
def verification():
    try:
        for user in this_user_detail:
            email=user['email']
            password=user['password']
            user = auth.sign_in_with_email_and_password(email,password)
            return user
    except:
          #this_user_id.clear()
          lit.write('The data entered is not valid')
    

def login_process():
        
        try:
            user1=verification()
            
            for user in this_user_detail:
                user_OTP=user['opt']
                
            name=database.child(user1['localId']).child('AccountName').get().val()   
            mfa_check=database.child(user1['localId']).child("mfa").get().val()
                
                
                #calling users unique key saved to their secure account
            OTP=database.child(user1['localId']).child("OTP").get().val()
                #saving the OTP in a variable to chekc
            OTP_now=Authentication.mfa.generatepin(OTP)
                #lit.sidebar.write(OTP_now)
            if mfa_check==0:
                lit.warning("""FANG uses time-based one-time passcodes (TOTP) that are compliant with all major authenticator apps uncluding Authy, Google Authenticator and Microsoft Authenticator.""")                  
                lit.write("Open or Download your favourite Authentication App")
                lit.write("Add account by scanning QR code")\
                        
                    #generate the QR Code
                    #with mfa_column:
                Authentication.mfa.generate_qr(OTP) #generate QR code
                                                
                if user_OTP == OTP_now:
                            lit.success("Hi " + name +" You are now verified and logged in!")
                            #success messages and updating MFA status to 1
                            database.child(user1['localId']).update({"mfa":1})
                            with lit.spinner('We are deleting your QR code for security reasons'):
                                time.sleep(5)
                                Security.remove_QR.del_QR()
                                lit.success('Done!') 
                                logged_in={'localID':user1['localId']}
                                this_user_id.append(logged_in)
                                lit.session_state['loggedIn']=True
                                
                else:
                            lit.error("🔥 Codes not matching")
                                    
            else:
                    
                    mfa_check=database.child(user1['localId']).child("mfa").get().val()
                    
                    login_button=lit.button("Login")
                    
                    if login_button and user_OTP == OTP_now:
                        lit.success("Hi " + name +" You are logged in!")
                        logged_in={'localID':user1['localId']}
                        this_user_id.append(logged_in)  
                        lit.session_state['loggedIn']=True
                    
                        
                    else:
                        lit.error("🔥 Codes not matching")
            
        except:
            lit.error("Please enter the valid credentials")                             
                
        
        
              
            

      
                
                
                
                    
                    

            





def reset_password():
    with lit.form("Reset_Password"):        

        lit.subheader("Reset Password")
            
        # User input
        email=lit.text_input("Enter your email address")
        reset_button =lit.form_submit_button("Reset")

        if reset_button:
            lit.success("Instructions were sent to your email")
    