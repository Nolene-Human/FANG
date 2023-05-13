

   ## ------------------THIS IS 'TIPS' TAB ------------------------------##
 ## ----------------- Called from Launch.py  --------------------------------##
 
# - FUTURE DEVELOPMENT - #
# No Future Development planned 
## ______________________________________##

import streamlit as lit

def tips():

    lit.markdown("# Good CyberHygiene Tecniques + Tips")
    select = lit.selectbox("Select a topic from the dropdown list?",(" ","Maintain good password hygiene","Update systems and software","Multi Factor Authentication","Keep up-to-date on phishing/security training and awareness","Implement 'Zero Trust'","Anti-Virus"))

    if select == "Maintain good password hygiene":
        lit.markdown("FANG can help you manage all those passwords, ensure they are strong and enable features that can protect your account from attackers")
        lit.subheader("Some reason why you should")
        lit.markdown("- Block Web and Email Threats")
        lit.markdown("- Keep Hackers of your PC")
        lit.markdown("- Protect you from Snoops")
        lit.markdown("- Shop and Bank saver")        
        lit.subheader("How to:")
        lit.write("Use Password Management Tools")
        lit.markdown("Consider Passphrase or Random common words for your password")
        lit.image("Art/Pictures/passphrase.png")

    elif select =="Update systems and software":
        lit.subheader("Some reason why you should")
        lit.markdown("- Enhance Security")
        lit.markdown("- Enhance Performance")
        lit.markdown("- Avoid Hardware Problems")
        lit.markdown("- Avoid losing features")
        lit.markdown("- Avoid Data loss")
        lit.subheader("How to:")
        lit.write("""Visit the software or device company website to see if there is any updates. If you have an application installed see if you have any notifications to update. 
        Some apps or devices will notify you through settings.""")
        lit.write("❗ Don't forget to do this for all devices connected to the internet.")

    elif select == "Multi Factor Authentication (MFA)":
        lit.subheader("Some reason why you should")
        lit.markdown("- Reduce the chances of a data breach")
        lit.markdown("- Secure Against Identity Theft Via Stolen Passwords")
        lit.markdown("- Enable Your Other Security Measures To Do Their Job Properly")
        lit.markdown("- Stay compliant")
        lit.subheader("What it Does")
        lit.image("Art/Pictures/mfa.png")
        lit.write("MFA provides more than one way to verify your login, hackers are unable to access your accounts without knowing all three keys at the time you log in")
        lit.subheader("Link to explain MFA")
        lit.markdown("[Multi Factor Authentication](https://www.youtube.com/watch?v=nc7fpGJsE1g)")
        lit.subheader("Link to tools that can be used for all types of accounts")
        lit.markdown("[Microsoft Multi Factor Authenticator](https://www.microsoft.com/en-nz/p/microsoft-authenticator/9nblgggzmcj6")
        lit.markdown("[Twilio](https://authy.com/guides/twilio/)")
        lit.markdown("[LastPass](https://www.lastpass.com/)")
    
    elif select == "Keep up-to-date with phishing/security training and awareness":
        lit.subheader("Some reason why you should")
        lit.markdown("- Protecting your personal and financial information")
        lit.markdown("- Protecting your business")
        lit.markdown("- Staying ahead of evolving threats")
        lit.markdown("- Will help you stay compliant with regulations and standards")
        lit.subheader("Register to a newsletter")
        lit.markdown("[Cloudflare]https://blog.cloudflare.com/)")

    elif select == "Anti-Virus":
        lit.subheader("Some reason why you should")
        lit.write("Detect and remove computer Virus and anti-malware from your device")
        lit.markdown("- Malware & Virus Protection")
        lit.markdown("- Defence Against Data Thieves")
        lit.markdown("- Increases Your Computer’s Lifetime")
        lit.markdown("- Comprehensive Threat Protection")
        lit.subheader("What it Does")
        lit.markdown("- Stop threats in Real time")
        lit.markdown("- Block Web and Email Threats")
        lit.markdown("- Keep Hackers of your PC")
        lit.markdown("- Protect you from Snoops")
        lit.markdown("- Shop and Bank saver")
        lit.markdown("- Alerts and Reports")
        lit.subheader("Link's to some of the top Anti-Virus Software")
        lit.write("[AVG](https://www.avg.com/en-ww/homepage#pc)")
        lit.write("[Kaspersky](https://www.kaspersky.com.au/)")
        lit.write("[McAfee](https://nz.norton.com/store)")
        lit.write("[Norton](https://nz.norton.com/store)")
        lit.write("[Bitdefender](https://www.bitdefender.com/)")

    else:
        lit.write("Starting somewhere is better than nowhere")



