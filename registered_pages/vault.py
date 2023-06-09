import streamlit as lit

import random
import Authentication.user_login
import Firebase.firebaseconfig


this_user=Authentication.user_login.return_this_user()
database=Firebase.firebaseconfig.firebase_database()

for users in this_user:
    local=users['localID']
    

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

def add_password_form():
    

    
    with lit.form("Enter Vault",clear_on_submit=True):
                                                 
        account_name=lit.text_input("Enter Account Name: ")
        account_web=lit.text_input("Enter link to account")
        account_username=lit.text_input("Enter Username: ")
        password_entered = lit.text_input("Enter Password: ")
        save_to_vault=lit.form_submit_button("Save to Vault")

    if save_to_vault and account_web == "" and account_username=="" and account_name=="" and password_entered=="" :
        lit.write("This form needs all the data")
        
    if save_to_vault:
        vault_entry={"vault_name" : account_name,"vault_web":account_web,"account_username":account_username,"vault_password":password_entered}
        database.child(local).child("vault").push(vault_entry)
        
