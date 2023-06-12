import streamlit as lit
from streamlit_extras.stodo import to_do



key_comms={}
ticklist={}
threats={}


def plan():
    column1,column2=lit.columns(2)

    lit.subheader("Cybersecurity Plan")
    plan=column1.button("generate the plan")

    # clear=column2.button("clear your plan")
    # if clear:
    #     key_comms.clear()
    #     ticklist.clear()
    #     threats.clear()
    if plan:
        lit.markdown("**Goals & Plan to prevent cyber attacks**")

        for goal in ticklist.values():
                    lit.write(goal)

        lit.markdown('----------------------')

        lit.markdown("**Potential threats**")
        lit.write("These are the treats we are monitoring:")
        for threat in threats.values():
                    lit.write(threat)


                #lit.markdown('----------------------')

                #lit.markdown("**Security policies**")

        lit.markdown('----------------------')
        lit.markdown("**Key Contacts and Communication Plan**")
        try:
                    business=key_comms['key_business']
                    key_contact=key_comms['key_contact']
                    key_email = key_comms['key_email']

                    lit.markdown("*In the event that "+ business + " falls victim to a cybersecurity attack "+ key_contact +" will contact you either by phone or from "+ key_email +" explaining the sitution and how we are responding to the issue.*")
        except:
                    lit.warning("Your key contacts gets generated from your incident response plan")


    else:
        lit.warning("The information in this documents gets populated from completing the incident response plan")

## ______________________________________________________________________________________________________________________##

def comms_plan():

    with lit.expander("Setting Key Contacts and Communication Plan"):

        lit.write(""" You would want to set up a communication strategy in the event of an attack. This communication should be between two parties or devices that are using a
        path or method different from the primary communication used inside your organisation. If you don't have this in place, you might need to spend some time to set this up first.
        Please complete the below with this information. """)

        business=lit.text_input("Enter your business name: ")
        key_email=lit.text_input("Enter email account not linked to any of your office accounts: ")
        key_contact=lit.text_input("Enter name of the key person who will send the communications: ")
        key_IT=lit.text_input("Who is your techinical support: ")
        save_comms = lit.button('Save')

        if save_comms:
            your_comms={'key_business':business,'key_email':key_email,'key_contact':key_contact,'key_it':key_IT}
            key_comms.update(your_comms)
            lit.write(key_comms)


## ______________________________________________________________________________________________________________________##

def plan_ticklist():

    with lit.expander("Goals & Plan to prevent cyber attacks"):

        lit.warning("By going throught the following tick list you are confirming that you and your business have implemented and are following the minimum Cybersecurity Protocols to protect your network and the information you are responsibile for.")
        lit.success("You can do this in phases or only do some, once you have ticked the list your Cybersecurity Plan will be updated with the information to export and share.")
        password=to_do(
                [(lit.write, ":floppy_disk: Secure passwords with MFA: My passwords meets the minimum strenght settings and are securely saved using a password management tool. All data is accessed using Multi-factor authentication")],
                                "password",
                            )
        assets=to_do(
                [(lit.write, ":floppy_disk: Identify critical assets: I have identified and are monitoring all assets in my network.")],
                                "assests",)
        training=to_do(
                [(lit.write, ":floppy_disk: Conduct awareness training : I build awareness among staff and attend training to ensure we stay on top of current threats.")],
                                "training",)
        response=to_do(
                [(lit.write, ":floppy_disk:  Establish response actions : I build and run table-top exercises for a strong response action plan  in the event of a cybersecurity breach. ")],
                                "response", )
        access=to_do(
                [(lit.write, ":floppy_disk:  Implement access control : My home and personal devices are segregated from my business devices, and only authorised and authenticated users have access to business devices.")],
                                "access",
                            )
        protect=to_do(
                [(lit.write, ":floppy_disk: Deploy protection tools : All devices are kept up to date with the latest patches. Business devices have strong threat management tools implemented like firewalls and antivirus software. ")],
                                "protect",
                            )
        monitor=to_do(
                [(lit.write, ":floppy_disk: Monitor : I use FANG to monitor my network for any vulnerabilities in my network ")],
                                "monitor",
                            )

        if password:
            passw={1:"My passwords meets the minimum strenght settings and are securely saved using a password management tool"}
            ticklist.update(passw)
        if assets:
            asset={2:"I have identified and are monitoring all assets in my network."}
            ticklist.update(asset)
        if training:
            train={3:'I build awareness among staff and attend training to ensure we stay on top of current threats.'}
            ticklist.update(train)
        if response:
            resp={4:'I build and run table-top exercises for a strong response action plan  in the event of a cybersecurity breach.'}
            ticklist.update(resp)
        if access:
            acc={5:'My home and personal devices are segregated from my business devices, and only authorised and authenticated users have access to business devices.'}
            ticklist.update(acc)
        if protect:
            prot={6:'All devices are kept up to date with the latest patches. Business devices have strong threat management tools implemented like firewalls and antivirus software.'}
            ticklist.update(prot)
        if monitor:
            moni={7:'I use FANG to monitor my network to ensure proactive response against vulnerabilities.'}
            ticklist.update(moni)

def identify_threats():

    with lit.expander("Identify your risks"):


        # -- tick box for users input -- #

        social_Engineering = lit.checkbox('Do you use Emails?')
        thirdparty_Exposure = lit.checkbox('Do you work from home on other business data?')
        configuration = lit.checkbox('Are you nervous doing any configuration on your devices?')
        cloud = lit.checkbox("Do you use any websites or access applications through an online connection?")
        things=lit.checkbox("Do you have any smart devices that connect to the network or you control through an application (tv's , lights, poweradaptors)?")
        ransomeware=lit.checkbox("Do you work with sensitive or private data, that can't be seen by other except those it is intended?")
        data =lit.checkbox("Do you share data or any information over the internet?")

        lit.markdown("---")

        if social_Engineering:
            email={1:"Social Engineering through email phishing and impersonation."}
            threats.update(email)

        if thirdparty_Exposure:
            third={2:"Exposure to Third-parties unprotected networks."}
            threats.update(third)

        if configuration:
            config={"Configuration mistakes from devices joining the network."}
            threats.update(config)

        if cloud:
            cl={"Cloud Vulnerabilities working with third party or customers web application."}
            threats.update(cl)

        if things:
            thi={"Internet of Things : devices weak security."}
            threats.update(thi)

        if ransomeware:
            ran={"Ransomware."}
            threats.update(ran)

        if data:
            dat={"Poor Data Management."}
            threats.update(dat)
