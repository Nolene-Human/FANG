import streamlit as lit

import random
import Authentication.user_login
import Firebase.firebaseconfig

this_user=Authentication.user_login.return_this_user()
database=Firebase.firebaseconfig.firebase_database()
auth= Firebase.firebaseconfig.firebase_auth()



for users in this_user:
    local=users['localID']


if 'vault_read' not in lit.session_state:
                lit.session_state['vault_read']=False


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

def add_vault_form():
    

    user=auth.sign_in_with_email_and_password('test1@gmail.com','D4nc3r$')
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
        database.child(user['localId']).child("vault").push(vault_entry)
        
def cud_vault():
    lit.session_state['vault_read']=True
    
    save_vault_edit=lit.button("Save Changes")
    
    for users in this_user:
        local=users['localID']

    user=auth.sign_in_with_email_and_password('test1@gmail.com','D4nc3r$')
    try:
        #get_vault=database.child(local).child('vault').get()
        get_vault=database.child(user['localId']).child('vault').get()

        show_dataframe_vault=[]
    
        for vault in get_vault.each():
            
            val_result=vault.val()

            username_result=val_result["account_username"]
            usern_result=val_result["vault_name"]
            password_result=val_result["vault_password"]
            web_result=val_result["vault_web"]

            read_vault_list={"Username":username_result, "Vault Name":usern_result,"Vault Password":password_result,"Web Link":web_result}
            
            show_dataframe_vault.append(read_vault_list)
             

        for vault_item in get_vault.each():
            drop_vault=(vault_item.key(),'1')
            read,delete = lit.columns([2,1])
            with read:
                vault_to_edit, confirm_vault_edit = lit.columns(2)
                with vault_to_edit:
                    save_edit_vault_data=lit.data_editor(vault_item.val(), key=drop_vault)
            
                
                if save_vault_edit:                                         
                    database.child(local).child('vault').child(vault_item.key()).update(save_edit_vault_data)
                    #database.child(user['localId']).child('vault').child(vault_item.key()).update(save_edit_vault_data)
                                   
            with delete:
                    delete_vault=(vault_item.key(),'3')
                    vault_delete_option=lit.radio("Delete",("No","Yes"),key=delete_vault,horizontal=True)
                    if vault_delete_option == 'Yes' and save_vault_edit:
                        database.child(local).child('vault').child(vault_item.key()).remove()
                        #database.child(user['localId']).child('vault').child(vault_item.key()).remove()
                    if vault_delete_option == 'Yes':
                        lit.warning("🚨 Are you sure, this account will be deleted after you saved changes")
 
    except:
        lit.write("No data in your vault, yet")

