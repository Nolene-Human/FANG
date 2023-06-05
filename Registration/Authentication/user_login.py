
import streamlit as lit


def login_form():

  with lit.form("User_Login"):        

        lit.subheader("Login")
            
        # User input
        email=lit.text_input("Your Email address")
        password=lit.text_input("Confirm password",type="password")
        login_button =lit.form_submit_button("Login")

        if login_button:
            lit.success("You are logged in")



def verify_user():
   lit.write("verify user")


def reset_password():
    with lit.form("Reset_Password"):        

        lit.subheader("Reset Password")
            
        # User input
        email=lit.text_input("Enter your email address")
        reset_button =lit.form_submit_button("Reset")

        if reset_button:
            lit.success("Instructions were sent to your email")
    