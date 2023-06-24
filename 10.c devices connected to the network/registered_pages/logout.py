import streamlit as lit

def logout():
    logout=lit.sidebar.button('logout')

    if logout:
       
        lit.write("you are logged out")