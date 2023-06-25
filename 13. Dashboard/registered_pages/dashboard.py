import streamlit as lit
from streamlit_extras.stodo import to_do

import time
# extract information about running processes and system utilization
import psutil # process and system utilities
import nmap

import registered_pages.devices
import Firebase.firebaseconfig



def dashboard():
    col1,col2, col3 = lit.columns(3)

    with col1:
        lit.markdown('**Have you?**')
        to_do([(lit.write, ":floppy_disk: Save your passwords ")],
                        "password-todo",)

        to_do([(lit.write, ":computer: Scan your network")],
                        "scan",)

        to_do([(lit.write, ":card_index_dividers: Segment your network")],
                        "segment",)

    with col2:
        lit.markdown("**Network Activities, data of total bytes sent and received**")
        count=6
        network_activity=[]
        
        # psutil.net_io_counters() returns network I/O statistics as a namedtuple
        netStats1 = psutil.net_io_counters()
        # Getting the data of total bytes sent and received
        dataSent = netStats1.bytes_sent
        dataRecv = netStats1.bytes_recv

        # Running a loop to get the data continuously
        while count > 0:

            # Delay for one second
            time.sleep(1)

            # Getting the network i/o stats again to 
            # count the sending and receiving speed
            netStats2 = psutil.net_io_counters()
            
            # Getting the data of total bytes sent and received
            # Upload/Sending speed
            uploadStat = netStats2.bytes_sent - dataSent
            # Receiving/Download Speed
            downloadStat = netStats2.bytes_recv - dataRecv

            network_reading={'Upload Speed':uploadStat,'Download Spee':downloadStat}
            network_activity.append(network_reading)
            count -= 1
    

    col2.dataframe(network_activity)

    with col3:
        lit.markdown('**New Devices on your network**')

        auth=Firebase.firebaseconfig.firebase_auth()    
        database=Firebase.firebaseconfig.firebase_database()
    
        user=auth.sign_in_with_email_and_password('test1@gmail.com','D4nc3r$')
        saved_count = 0
        scan_count = 0

        get_your_devices=database.child(user['localId']).child('Devices').get()
        for your_devices in get_your_devices:
            saved_count+=1

        new=nmap.PortScanner()         
            
        new.scan(hosts='192.168.1.0/24', arguments='-sn')
                 
        for host in new.all_hosts():
            scan_count+=1

        
        col3.write('Number of new devices detected on your network:' )
        col3.write((scan_count-saved_count))




