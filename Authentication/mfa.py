import streamlit as lit
import time
import pyotp
import qrcode



def key():
    key=pyotp.random_base32()
    return key

def generate_qr(key):
    uri=pyotp.totp.TOTP(key).provisioning_uri(name="FANG",issuer_name="FANG App")

    #print(uri)
    #qrcode.make(uri).save("QRCode.png")
    qrcode.make(uri)

def generatepin(key):
    totp=pyotp.TOTP(key)
    mfacode=(totp.now())
    return mfacode