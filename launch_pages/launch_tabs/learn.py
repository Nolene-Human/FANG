   ## ----------------------------------------THIS IS 'LEARN TAB ------------------------------------------------------##
 ## -------------------------- Called from Launch.py when user select the Learn tab ------------------------------------##
 
# - NO FUTURE DEVELOPMENT PLANNED - #

## ______________________________________________________________________________________________________________________##

import streamlit as lit
from PIL import Image #used to display images on page 

def learn():
    
    
    col1,colb=lit.columns([1,6])

    triangle=Image.open("Art/Pictures/Triangle.png")
    col1.image(triangle)
    
    colb.header("Why are you under attack, and how FANG can help you secure your network")

# ---------- Key Terminology ---------------#
       


    
    
    lit.text("KEY WORDS TO TAKE NOTE : ")
    col2,col3= lit.columns(2) 
    
    
    col2.write("""
            - Cyber Threats
            - Cyber Attacks
            - Gateway
            - IP Address
            - Mac Addresses
            """)

    col3.write(""" 
        - Internet devices
        - Network        
        - Ports
        - Integrity
        - Availability
        - Confidentiality"""
    )

    lit.markdown("---")

# ---------- Key Ideas ---------------#  
    
    lit.write("In this section you will aquire the basic knowledge to confidently manage your own home network or communicate with technical support on this matter.")
    lit.markdown("#### Why would ANYONE want to attack you?")

    lit.write("""In the book The Art of Attack by Maxi Reynolds, a very successful social engineering in CyberSecurity states it well""")
    lit.write("""In the book [The Art of Attack](https://www.amazon.com/Art-Attack-Attacker-Security-Professionals/dp/1119805465) by Maxi Reynolds, a very successful social engineering in CyberSecurity states it well""")
                    
    lit.write("Your information or the information you have access to is crucial for cybercriminals.")

    lit.text("\n")
    
    lit.markdown("---")

    lit.markdown("#### What is a Network and Why Should I care?")
    lit.markdown("""
    You are connecting to the internet via a DEVICE through a PORT.
     The DEVICE connecting you to the internet is called a WIFI ROUTER. 
    The Port is like a DOOR to and from the Internet World. 
    Your Wifi Router is also commonly refered to as your GATEWAY.""",)
    lit.markdown("#### Each device will have a DOOR -> connected to your GATEWAY -> leading to the World Wide Web and all the hackers that live there.")

    lit.markdown("---")

    lit.markdown("""
    Your Gateway will assign each device on your network an address to identify and communicate with, this is called an IP ADDRESS. 
    Each device will have a unique IP ADDRESS and a MAC ADDRESS""")
    
    lit.markdown("#### The router assign a devices and IP address and a Manufacturer assigns the Mac Address")
    
    lit.markdown("---")

    lit.markdown("""
    Through these unique numbers we can identify the devices on your network (inlcuding its known vulnerabilites and uses).""") 

    lit.markdown("#### This collective group of devices are called your NETWORK.")

    lit.markdown("---")

    lit.markdown("""
    Hackers can without your consent, connect, communicate or monitor your NETWORK.  
    Once in your network, they can disguise themselves, reroute your internet activities to their servers in turn see your activities. This will include accounts, usernamesand password.""")
    
    lit.markdown("#### These malicious activities are called CYBER THREATS.")

    lit.markdown("---")

    lit.markdown("""
    #### This is why you need to monitoring your Network.

    This tool will help you take the basic necessary precautions to avoid the most common *CYBER ATTACKS* by scanning your internal network for vulnerabilities and providing tips and learning pages to help you protect 
    your network.

    Well Done for taking the first step in securing yourself agains Cyber Threats ! """,True)



   

   