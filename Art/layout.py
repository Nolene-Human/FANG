
import streamlit as lit

def layout():
 lit.set_page_config(
        page_title="F A N G",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': '',
            'Report a bug': "",
            'About': "# You will never look back"
        }
    )
    