![HI](/hi.PNG)


# Vulnerability_Scanner
## by Nolene Human 
date: 31/01/2023
This application is built of the back of a Bachelor of Software Engineering Cybersecurity assignment to investigate a solution with recomended improvements.

# IMPORTANT TO READ
This application uses nmap pentesting techniques to collect data from your network. It is designed to use the basic Nmap functionswith an additional feature to educate users on cybersecurity. Therefor it is important to note that this assignemnet is NOT a vulnerability management solution but a subset process that scann and identifying vulnerabilities, misconfiguration or flaws in the users network.


# Introduction
Since 2020 the working landscape has changed as more and more people are starting to work from home. This means that cyber threats and the proactive measures to prevent security breaches are no longer only a business networks issue, but also the responsibility of the employee and that of a contractor working on their private network. There are multiple solutions to secure connections between these networks, but due to the lack in the technical understanding and fear to adjust the their own network security are creating a huge risk. 

Users, like Sally, an accounts payable clerk working more and more from home for a small organisation. Darren, as a contractor working with multiple organisations from shared spaces in various locations, and Charlie, a small business onwer who provide virtual assistant to various clients.

Therefor I am suggesting a simple first line of defence solutions to protect my user from the most common cyber threats.  A vulnerability scanner with a built in training tool designed for non-technical users together with easy to use instructions on how to secure their network.  

Must Have: Vulnerability scanner that will look for know threats on the most common issues faced by a Work from Home network environments. Simple and easy to understand. Recommendations on how to fix the know / identified risks. 

Should Have: Education tool for user on the best practises used to secure an environment. 

Could Have: Test and report on the current environment based on best practices. 

Won’t Have: Vulnerability Management tool


# How to Install the Project
This Application uses Python, Nmap together with Streamlit as its stack tools. 
Database is part of future development

** Helpful tip: If you use Anaconda you can replicate the environment by importing the Nolene_vulenrability_env.yml file into your environment to get all dependancies.
-- 
Go straight to 'How to Run project' 

## Requirements
Python
Python 3.11.1

Nmap
Nmap version 7.93 ( https://nmap.org )

Streamlit
Streamlit, version 1.17.0

## Instilations and Dependancies

## Back End

** Python: 

[Download Python | Python.org](https://www.python.org/downloads/)

** Scanning Tools: 

- pip install python-nmap

- pip install ifcfg

- pip install getmac


## Front End

### Web interface tools

**Streamlit

**Start Here

[https://docs.streamlit.io/library/get-started](https://docs.streamlit.io/library/get-started)

[Installation - Streamlit Docs](https://docs.streamlit.io/library/get-started/installation)

pip install streamlit

** Anaconda

[Installing on Windows — Anaconda documentation](https://docs.anaconda.com/anaconda/install/windows/)

* in folder project folder : `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`


** Other

- pip install requests
- pip install streamlit-extras


### Animation
pip install streamlit-lottie

# How Run the Project


# How to Use the Project

Create a virtual environment in Anaconda

Run via open terminal

Navigate to the folder you saved/downloaded this project

run using command : streamlit run Welcome.py

Anaconda will navigate to the application opened on your loacalhost:()


Live Preview:


# Not in Project Scope

# Credits

HackerSploit. (2019, January 21). Python3 For Pentesting - Developing An Nmap Scanner [Video]. YouTube. https://www.youtube.com/watch?v=1lh_SkY8cHk&t=320s 

How to find your default gateway IP address . (2010, November 8). Lifewire. https://www.lifewire.com/how-to-find-your-default-gateway-ip-address-2626072 

Python | Get a list as input from user . (2023, January 11). GeeksforGeeks. https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/?ref=leftbar-rightbar 

IBM: 2021 X-force threat intelligence index. (2021). Network Security, 2021(3), 4-4. https://doi.org/10.1016/s1353-4858(21)00026-x 

EC-Council (2022) Understanding the five phases of the penetration testing process , Cybersecurity Exchange. Available at: https://www.eccouncil.org/cybersecurity-exchange/penetration-testing/penetration-testing-phases/ (Accessed: December 7, 2022). 



# Badges

(looking into it)

# How to Contribute to the Project
