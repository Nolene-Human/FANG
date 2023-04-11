import streamlit as lit

def admin():

    lit.title("with Great Power comes Great Responsibily")
    lit.sidebar.success("Admin")

    lit.write("Welcome Admin to your new page")