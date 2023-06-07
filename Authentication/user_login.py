
## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - no future developments
## ______________________________________________________________________________________________________________________##

import streamlit as lit
import time
import pyotp

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase SDK's
import Authentication.mfa #otp functions
import Security.remove_QR
## ______________________________________________________________________________________________________________________##




def login_form():
    login_column, mfa_column = lit.columns(2)

    database=Firebase.firebaseconfig.firebase_database()
    auth= Firebase.firebaseconfig.firebase_auth()
    
    #with login_column.form("User_Login"):        
    with login_column:
        lit.subheader("Login")
            
        # User input
        email=lit.text_input("Your Email address")
        password=lit.text_input("Confirm password",type="password")
        
        mfa_column.subheader("Verification")
        user_OTP=mfa_column.text_input("Please enter OTP Code",type="password")
        
        #check_mfa=login_column.checkbox(":unlock: Register for OTP")
              
        if email == "" or password=="" or user_OTP=="":
                lit.warning("Please enter all fields")

               
        if email != "" and password!="" or user_OTP!="":
            try:
                user = auth.sign_in_with_email_and_password(email,password)
                name=database.child(user['localId']).child('AccountName').get().val()   
                mfa_check=database.child(user['localId']).child("mfa").get().val()
                
                #calling users unique key saved to their secure account
                OTP=database.child(user['localId']).child("OTP").get().val()
                #saving the OTP in a variable to chekc
                OTP_now=Authentication.mfa.generatepin(OTP)

                if mfa_check==0:
                    
                    mfa_column.warning("""FANG uses time-based one-time passcodes (TOTP) that are compliant with all major authenticator apps uncluding Authy, Google Authenticator and Microsoft Authenticator.""")                  
                    mfa_column.write("Open or Download your favourite Authentication App")
                    mfa_column.write("Add account by scanning QR code")
                        
                    #generate the QR Code
                    with mfa_column:
                        Authentication.mfa.generate_qr(OTP) #generate QR code
                                                
                        if user_OTP == OTP_now:
                            mfa_column.success("Hi " + name +" You are now verified and logged in!")
                            #success messages and updating MFA status to 1
                            database.child(user['localId']).update({"mfa":1})
                            with lit.spinner('We are deleting your QR code for security reasons'):
                                time.sleep(5)
                                Security.remove_QR.del_QR()
                                mfa_column.success('Done!')
                    
                        else:
                            lit.error("🔥 Codes not matching")
                                    
                else:
                    
                    mfa_check=database.child(user['localId']).child("mfa").get().val()
                    
                    login_button=mfa_column.button("Login")
                    
                    if login_button and user_OTP == OTP_now:
                        
                        mfa_column.success("Hi " + name +" You are logged in!")

                
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
    