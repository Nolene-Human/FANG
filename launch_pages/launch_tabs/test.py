
   ## ----------------------------------------THIS IS 'TEST' TAB ------------------------------------------------------##
 ## -------------------------- Called from Launch.py when user select the test tab ------------------------------------##
 
# - FUTURE DEVELOPMENT - #
# - Add questionnaire so user are able to relate better to the treats 
# - Link each threat to a solution which will either be the TIPS or the SCANNER page 

# ______________________________________________________________________________________________________________________##

# -- FUTURE DEVELOPEMENT -- #


import streamlit as lit


def attacks_lit():



   lit.subheader("""
    Identify your risks:
        """)

    # -- tick box for users input -- #
   social_Engineering = lit.checkbox('Do you use Emails?')
   thirdparty_Exposure = lit.checkbox('Do you work from home on other business data?')
   configuration = lit.checkbox('Are you nervous doing any configuration on your devices?')
   hygiene = lit.checkbox("You don't have any network protection processes in place?")
   cloud = lit.checkbox("Do you use any websites or access data through an online connection?")
   mobile= lit.checkbox("Do use any online applications?")
   things=lit.checkbox("Do you have any smart devices that connect to the network or you control through an application (tv's , lights, poweradaptors)?") 
   ransomeware=lit.checkbox("Do you work with sensitave or private data, that can't been seen by other except those it is intended ?")
   data =lit.checkbox("Do you share data or any information over the internet?")
   procedures=lit.checkbox("You don't do any checks on your system?")

   

   lit.markdown("---")
   


    # -- if a tick box is checked the vulnerability is shown -- #
   if social_Engineering:
      lit.write("**Social Engineering**: this relies on you making a mistake by giving away your information (phishing and email impersonation)")
    

   if thirdparty_Exposure:
      lit.write("""**Third-party Exprosure** : You are working outside of a protected network, working from home as an employee or contractors.
                 This is making you a weak link in the newtork for the organisations you are working for""")
    
      
   if configuration:
      lit.write("""**Configuration Mistakes** : Not ensuring all your devices connected to the internet meets the minimum security configuration is a huge risk""")
    
   if hygiene:
      lit.write("""**Poor Cyber Hygiene** : Poor password, unprotected home networks makes for an easy target""")
     

   if cloud:
      lit.write("""**Cloud Vulnerabilities** : Web Application and Cloud Service breaches are increasing, default security settings were exposed, exposing ways for application and services
         to be hacked, with insufficient access control such as Multifactor Authentication (MFA) and casual trust between environments is making your devices easier to hack""")
      

   if mobile:
      lit.write("""**Mobile Device Vulnerabilities** : Malicious mobile application, coming sometimes from the organisations you working with can cause a risk in you network""")
     

   if things:
      lit.write("""**Internet of Things** : Malicious mobile application, coming sometimes from the organisations you working with can cause a risk in you network""")
      
   if ransomeware:
      lit.write("""**Randsomeware** : Through malicious software sent to you by an attacker data can be held for ransom, blocking you from accessing it until you have paid, or could provide details
      on how they have hacked your system and threat to release this to your clients.""")
    
   if data:
      lit.write("""**Poor Data Management** : Your or the companies you work for, data can be exploited for financial gain- this is different than ransomeware as the data is sold to a third party without your
      knowledge.""")
    

   if procedures:
      lit.write("""**Inadequate Post-Attack Procedures** : Not having a system or process in place to recover from any of these attacks could close your business or destroy your reputation.""")
      


   lit.markdown("---")



