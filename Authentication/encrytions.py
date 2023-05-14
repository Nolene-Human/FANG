
import hashlib
import registered_pages.ZeroTrustFunctions.passwordvault
import streamlit as lit

def hashlib(password):
    
    newpassword="my_password"
    # Add some random salt to make the hash stronger
    salt=registered_pages.ZeroTrustFunctions.passwordvault.generate_password()
    
    hashed_password = hashlib.sha256(salt.encode() + newpassword.encode()).hexdigest()
    hashed_user_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    
    if hashed_user_password == hashed_password:
        lit.write("#")        
