
import streamlit as lit
import pyotp #python OTP library
import qrcode


#generate user unique key that gets saved against their account when user register
def key():
    key=pyotp.random_base32()
    return key

#calls the key of the user (from database) and generates a QR code for the user to scan
def generate_qr(key):
    
    uri=pyotp.totp.TOTP(key).provisioning_uri(name="FANG",issuer_name="FANG App")
    qrcode.make(uri).save("QR.png")
    lit.image("QR.png",width=150)    


#based on the encryption key value a One time passcode is generated. This OTP generated when code is called match OTP on users application. 
def generatepin(key):
    totp=pyotp.TOTP(key)
    mfacode=(totp.now())
    return mfacode


