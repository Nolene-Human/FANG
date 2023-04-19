
# -- Using subprocess to run command prompt ipconfig on current device to show users default gateway IP address -- #
# -- FUTURE IMPROVEMENTS -- #
# -- The data displayed is not very user friendly and can be improved on -- #

import subprocess
import streamlit as lit
import ifcfg

def config_py():
    
  
    # Traverse the ipconfig information
    data = subprocess.check_output(['ipconfig']).decode('utf-8').split('\n')
    
    # Arrange the bytes data
    for item in data:
            print(item.split('\r')[:-1])


def config_lit():
    
    lit.markdown("**WOW** - this is a lot of information!") 
    lit.markdown("**NO PROBLEM** press - CNTR F - on your keyboard and type default gateway")
    lit.markdown("**ENTER TWICE -  until you find the Default gateway IP Address that looks something like - xxx.xxx.x.x -, CHANCES ARE - it is 192.168.1.1")


    # Traverse the ipconfig information
    data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
    
    # Arrange the bytes data
    for item in data:
        lit.write(item.split('\r')[:-1])
        if data == "Default Gateway":
            lit.write(data)
        

