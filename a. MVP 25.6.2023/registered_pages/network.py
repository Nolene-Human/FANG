import streamlit as lit
import nmap

def port_scanner():

    port_scanner=lit.checkbox("Run Port scanner")

    lit.markdown('**PORT SCANNER**')
    lit.write(""" Ports, explained simply is, a doorway through which applications communicate.
                There are various port numbers each are used for a specific purpose. 
                Ports allow for your computer to easily differentiate between different kinds of traffic. 
                For example emails go to a different port than webpages.
                Some ports you need open to be able to communicate with the internet.
                Others are not used in a home network and poses a threat. We can go ahead and close these.
                The following scan will show you all your open ports on your wifi followed with a list of ports that 
                we need to close with a list of the kind of cyber threats.\n\n
                
                """)

    scanner = nmap.PortScanner()

    lit.write("Vulnerable open ports on you Gateway")
    
    # -- Scan TCP open port on Device -- #
    
    if port_scanner:

        scanner.scan("192.168.1.1",'1-1024','-v -sS')
        lit.write("Open Ports on TCP ",scanner["192.168.1.1"]['tcp'].keys())
        #tcp.append(scanner["192.168.1.1"]['tcp'].keys())


        
        # -- Scan UDP open port on Device -- #
        scanner.scan("192.168.1.1",'1-1024','-v -sU')
        lit.write("Open Ports on UDP ",scanner["192.168.1.1"]['udp'].keys())  
        
        list_port=[{'port':'FTP','number':'20,21','threat':"Anonymous authentication, cross-site scripting, password brute force"},
                {'port':'SSH','number':'22','threat':"Brute forcing SSH credentials or using a private key to gain access to the target system"},
                {'port':'Telnet','number':'23','threat':"Allow users to connect to remote computers over the internet, vulnerable to malware, phishing, credential detection / brute force"},
                {'port':'MTP','number':'25','threat':"Vulnerable to spam and phishing"},
                {'port':'DNS','number':'53','threat':"Distributed Denial of Service (DDoS) attack, Hackers can use a device on your network or attack your network with an influx of traffic causing it to slow down or crash"},
                {'port':'TFTP','number':'69','threat':"Also use to transfer files, remote attackers can download files without authentication"},
                {'port':'SMB','number':'139, 137, 445','threat':"Is used to shared access to files and printers, and has mutliple vulnerabilities, so best to block it"},
                {'port':'HTTP / HTTPS','number':'443, 80, 8080, 8443','threat':"Don't block these if you except if you host your own webserver in your network, most people have an online service that host their websites"}]


        lit.dataframe(list_port,width=5500)


