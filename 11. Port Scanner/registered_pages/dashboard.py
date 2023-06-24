import streamlit as lit

from streamlit_extras.stodo import to_do



def dashboard():
    col1,col2, col3 = lit.columns(3)

    with col1:
        lit.write('Have you?:')
        to_do([(lit.write, ":floppy_disk: Save your passwords ")],
                        "password-todo",)
        
        to_do([(lit.write, ":computer: Scan your network")],
                        "scan",)
        
        to_do([(lit.write, ":card_index_dividers: Segment your network")],
                        "segment",)

    with col2:
        lit.write("New Devices on your network")

def monitor():

    lit.write("Monitoring you network")