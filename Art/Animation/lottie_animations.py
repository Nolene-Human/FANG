import json

import streamlit as lit
import requests # to be able to load animation from website
from streamlit_lottie import st_lottie

def load_animation(url:str):
        r=requests.get(url)
        if r.status_code != 200:
                return None
        return r.json()
    

