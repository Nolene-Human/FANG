import streamlit as lit

import random

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    
    nr_letters = 5
    nr_symbols = 5
    nr_numbers = 5

    password = []

    while nr_letters > 0:
        pass_lett = random.choice(letters)
        password.append(pass_lett)
        nr_letters -= 1

    while nr_numbers > 0:
        pass_num = random.choice(numbers)
        password.append(pass_num)
        nr_numbers -= 1

    while nr_symbols > 0:
        pass_sym = random.choice(symbols)
        password.append(pass_sym)
        nr_symbols -= 1


    random.shuffle(password)
    return("".join(password))

def add_password():
    lit.subheader("Password Management Tool")
    tab1, tab2 = lit.tabs(["|  Enter password ","|  Your accounts "])
            
    with tab1:
        password=lit.checkbox('Generate a Password')
        if password:
            lit.write(generate_password())
        
         
        with lit.form("Enter New Account"):
            account_name=lit.text_input("Enter Account Name: ")
            account_web=lit.text_input("Enter link to account")
            account_username=lit.text_input("Enter Username: ")
            password_entered = lit.text_input("Password: ",type="password")

            save_password=lit.form_submit_button("Save Entry")


    with tab2:        
        lit.write("List of Accounts")
        if save_password:
            lit.write("Account name: "+account_name)
            lit.write("Username: "+account_username)
            lit.write("Link: "+account_web)
            saved_password=lit.button("Show Password")
            if saved_password:
                lit.write(password_entered)
            