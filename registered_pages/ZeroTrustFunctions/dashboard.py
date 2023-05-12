import streamlit as lit
import uuid
import socket
import Scanners.findhostdetails


def dashboard():
    col1,col2, col3 = lit.columns(3)

    col1.subheader("This Machine")
    mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
        for elements in range(0,2*6,2)][::-1]))

    col1.write("Mac Address : " + mac_addr) 

        # -- get the devices mac address and print for user using socket

    try:
            hostname = socket.gethostname()
            col1.markdown("Your Computer Name is : " + hostname)

    except:
          col1.write("Unable to get Hostname and IP")


    col1.write("Your device ip address is : "+ Scanners.findhostdetails.ip_address_lit())

    col2.subheader("Network Devices")
    col2.write("Your scan on the 9/04/2023 identified 13 devices on your network")
    col2.write("The scan shows you have 14 devices connected today")

    col3.subheader("Network activities")
    col3.write("This shows the network activity in the last 24 hours")

