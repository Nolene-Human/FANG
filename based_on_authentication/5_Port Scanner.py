

import streamlit as lit
import nmap
import time

import Scanners.portscanner

# -- Streamlit Page Formatting -- # 
lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")

# -- Navigation bar -- # 
lit.markdown("# Scanner ")

scanner = nmap.PortScanner()



# -- This is carrying the gateway IP address entered when full device scann was done -- #

lit.header("When running this your device might ask you to continue in Admin Mode- : Please accept (Yes)  ")
if "gateway" not in lit.session_state:
    lit.session_state["gateway"]= ""

ip_addr2 = lit.session_state["gateway"]



lit.write("Your Gateway entered is : " , ip_addr2)

# -- Converting text to ip addr -- #
type(ip_addr2)




# -- Button to Run Scan -- #
if lit.button('Run'):
  if ip_addr2 =="":
    lit.error('There is no IP address specified, either enter the number below or do device scan to find your gateway IP Address', icon="🤖")

  else:
    # -- Print explenation while waiting for scan to complete -- #
    lit.write(""" Ports, explained simply is a doorway through which applications communicate
                There are various port numbers each are used for a specific purpose. 
                Ports allow for your computer to easily differentiate between different kinds of traffic. 
                For example emails go to a different port than webpages.
                Some ports you need open to be able to communicate with the internet.
                Others though, we can close.
                The following scan will show you all your open ports on your wifi followed with a list of ports that 
                we need to close with a a list of the kind of cyber threats.\n\n
                
                """)
    with lit.spinner('Wait while we scan...'):
      time.sleep(10)
      lit.success('Done!')

    # -- Scan TCP open port on Device -- #
    scanner.scan(ip_addr2,'1-1024','-v -sS')
    lit.write("Open Ports on TCP ",scanner[ip_addr2]['tcp'].keys())
 
    # -- Scan UDP open port on Device -- #
    scanner.scan(ip_addr2,'1-1024','-v -sU')
    lit.write("Open Ports on UDP ",scanner[ip_addr2]['udp'].keys())           
    
 
  # -- print the list of ports vulnerable to the most common hacks -- # 
    lit.subheader("Look at the list of port numbers. Are there any of the following ports listed? You might need to go and close them on your router")

    col1, col2, col3 = lit.columns(3)
    with col1:
      lit.subheader("Port")
      lit.write("FTP")
      lit.write("SSH")
      lit.write("Telnet")
      lit.write(" ")
      lit.write(" ")
      lit.write("MTP")
      lit.write("DNS")
      lit.write("FTP")
      lit.write("SMB")
      lit.write(" ")
      lit.write("HTTP / HTTPS")

    with col2:
      lit.subheader("Port Number")
      lit.write("20, 21")
      lit.write("22")
      lit.write("23")
      lit.write(" ")
      lit.write(" ")
      lit.write("25")
      lit.write("53")
      lit.write("69")
      lit.write("139, 137, 445")
      lit.write(" ")
      lit.write("443, 80, 8080, 8443 (except if you host your own webserver in your network, most people have an online service that host their websites)")

    with col3:
        col3.subheader("Threat")
        col3.write("Anonymous authentication, cross-site scripting, password brute force")
        col3.write("Brute forcing SSH credentials or using a private key to gain access to the target system")
        col3.write("Allow users to connect to remote computers over the internet, vulnerable to malware, phishing, credential detection, and credential brute force")
        col3.write("Vulnerable to spam and phishing")
        col3.write("Distributed Denial of Service (DDoS) attack")
        col3.write("Password spraying and unauthorized access, and denial of service (DoS) attacks.")
        col3.write("It could be exploited via the EternalBlue vulnerability, brute forcing SMB login credentials, exploiting the SMB port using NTLM Capture, and connecting to SMB using PSexec")
        col3.write("Vulnerable to SQL injections, cross-site scripting, cross-site request forgery")


# -- Asking user to manually enter the IP address if they have it -- #
ip_addr = lit.text_input("You can also run a scan on any ip address in your network, enter it here: ")

# -- Converting text to ip addr -- #
type(ip_addr)

if lit.button('Run on entered IP Address'):

    # -- Print explenation while waiting for scan to complete -- #
    lit.write(""" Ports, explained simply is a doorway through which applications communicate
                There are various port numbers each are used for a specific purpose. 
                Ports allow for your computer to easily differentiate between different kinds of traffic. 
                For example emails go to a different port than webpages.
                Some ports you need open to be able to communicate with the internet.
                Others though, we can close.
                The following scan will show you all your open ports on your wifi followed with a list of ports that 
                we need to close with a a list of the kind of cyber threats.\n\n
                
                """)
    with lit.spinner('Wait while we scan...'):
      time.sleep(10)
      lit.success('Done!')

    # -- Scan TCP open port on Device -- #
    scanner.scan(ip_addr,'1-1024','-v -sS')
    lit.write("Open Ports on TCP ",scanner[ip_addr]['tcp'].keys())
 
    # -- Scan UDP open port on Device -- #
    scanner.scan(ip_addr,'1-1024','-v -sU')
    lit.write("Open Ports on UDP ",scanner[ip_addr]['udp'].keys())           
    
 
  # -- print the list of ports vulnerable to the most common hacks -- # 
    lit.subheader("Look at the list of port numbers. Are there any of the following ports listed? You might need to go and close them on your router")

    col1, col2, col3 = lit.columns(3)
    with col1:
      lit.subheader("Port")
      lit.write("FTP")
      lit.write("SSH")
      lit.write("Telnet")
      lit.write(" ")
      lit.write(" ")
      lit.write("MTP")
      lit.write("DNS")
      lit.write("FTP")
      lit.write("SMB")
      lit.write(" ")
      lit.write("HTTP / HTTPS")

    with col2:
      lit.subheader("Port Number")
      lit.write("20, 21")
      lit.write("22")
      lit.write("23")
      lit.write(" ")
      lit.write(" ")
      lit.write("25")
      lit.write("53")
      lit.write("69")
      lit.write("139, 137, 445")
      lit.write(" ")
      lit.write("443, 80, 8080, 8443 (except if you host your own webserver in your network, most people have an online service that host their websites)")

    with col3:
        col3.subheader("Threat")
        col3.write("Anonymous authentication, cross-site scripting, password brute force")
        col3.write("Brute forcing SSH credentials or using a private key to gain access to the target system")
        col3.write("Allow users to connect to remote computers over the internet, vulnerable to malware, phishing, credential detection, and credential brute force")
        col3.write("Vulnerable to spam and phishing")
        col3.write("Distributed Denial of Service (DDoS) attack")
        col3.write("Password spraying and unauthorized access, and denial of service (DoS) attacks.")
        col3.write("It could be exploited via the EternalBlue vulnerability, brute forcing SMB login credentials, exploiting the SMB port using NTLM Capture, and connecting to SMB using PSexec")
        col3.write("Vulnerable to SQL injections, cross-site scripting, cross-site request forgery")