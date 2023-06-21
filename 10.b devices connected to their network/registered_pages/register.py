import streamlit as lit

import registered_pages.plan
import registered_pages.vault
import registered_pages.devices

def dashboard():
    dashboard, vault, plan, devices, network, account = lit.tabs(["|  dashboard ","|  password vault ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation ","|  your account "] )


    with dashboard:
        lit.write('dashboard')

## ______________________________________________________________________________________________________________________##
    with vault:
        lit.subheader("Password Management Tool")
        
        your_vault, enter_vault=lit.tabs(['Your Vault', 'Add to Vault'])
        

        with enter_vault:
            #UI/ UX
            left_vault,right_vault = lit.columns(2)
            
            #Strong password generator
            strong_password=registered_pages.vault.generate_password()

            new_password=left_vault.button("Generate a strong password")
            if new_password:
                right_vault.write(strong_password)  

    #********************************************************************************************************************#
        
        #New vault entry
            registered_pages.vault.add_vault_form() 
## ______________________________________________________________________________________________________________________##

        with your_vault:
            registered_pages.vault.cud_vault()

    with plan:
        
        plan,generate=lit.tabs(['Cybersecurity Plan','Incident Response Plan'])
        
        with plan:
            registered_pages.plan.plan()
            # save_plan=lit.button('Save Plan',key=now)
            # if save_plan:
            #     with open ("MyPlan.txt",'a') as file:
            #         file.write(registered_pages.plan.plan())
            #         file.close()
            #         pass
            #lit.download_button(label="Save Plan",data=save_plan,file_name='myplan.csv',mime='txt/csv',)

               
        with generate:
            registered_pages.plan.comms_plan()
            registered_pages.plan.plan_ticklist()
            registered_pages.plan.identify_threats()

    with devices:
        registered_pages.devices.devices_scan()

    with network:
        lit.write('network')
    
    with account:
        lit.write('account')

        