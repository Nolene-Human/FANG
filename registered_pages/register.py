import streamlit as lit

import registered_pages.plan
import registered_pages.vault


def dashboard():
    dashboard, vault, plan, devices, network, account = lit.tabs(["|  dashboard ","|  password vault ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation ","|  your account "] )


    with dashboard:
        lit.write('dashboard')

## ______________________________________________________________________________________________________________________##
    with vault:
        lit.subheader("Password Management Tool")

        #UI/ UX
        left_vault,right_vault = lit.columns(2)
        
        #Strong password management generator
        strong_password=registered_pages.vault.generate_password()

        new_password=left_vault.button("Generate a strong password")
        if new_password:
            right_vault.write(strong_password)  

    #********************************************************************************************************************#
        
        #New vault entry
        with left_vault:
            registered_pages.vault.add_password_form() 
## ______________________________________________________________________________________________________________________##
    with plan:
        lit.write("this is the plan")

    with devices:
        lit.write('devices')

    with network:
        lit.write('network')
    
    with account:
        lit.write('account')

        