import streamlit as lit

def registration_form():

    with lit.form("Lets get Registered"):        

            lit.subheader("Lets get Registered")
                
                # User input
            email=lit.text_input("Your Email address")
            password=lit.text_input(":pushpin: We encourage STRONG PASSWORDS",type="password",help="As a minimum this password would need, At least 6 characters, Should contain a $ @ # ! symbol, and have at least one Uppercase")
            confirmpass=lit.text_input("Confirm password",type="password")
            handle=lit.text_input("Your Network Name : ")
            register_btn =lit.form_submit_button("Register")
            
                
                # Rules and Checks once user press the 'register' button 
            if register_btn:
                  lit.success("You are Registered")