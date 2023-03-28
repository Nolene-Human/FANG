# importing the module
import subprocess

import streamlit as lit

# -- Page UI -- #
lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")


lit.markdown("# List of Application on your Device ")

lit.write ("The scan starts automatically and will take a few minutes to gather the information.")

# traverse the software list
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)

# try block
try:
	
	# arrange the string
	for i in range(len(a)):
		lit.write(a.split("\\r\\r\\n")[6:][i])

except IndexError as e:
	lit.write("All Done")


lit.write("""
## How To Remove Malware\n
Do-It-Yourself
Stop shopping, banking, and doing other things online that involve usernames, passwords, or other sensitive information — until you get your device cleared of any malware.
Check to see if you have security software on your device — if not, download it. Find recommendations from independent review sites by doing a search online. Also ask friends and family for recommendations. Some software that claims to be security software to protect you from malware is malware, so it’s important to do your research.
Make sure your software is up to date. Check that all software — the operating system, security software, apps, and more — is up to date. Consider turning on automatic updates so your software always stays up to date.
Scan your device for malware. Run a malware or security Delete anything it identifies as a problem. You may have to restart your device for the changes to take effect. Run your scan again to make sure everything is clear. If the scan shows there are no more issues, you’ve likely removed the malware.
If you’re not able to fix your device with steps 1-4, steps 5 and 6 may resolve the issue. When using either of these options, you risk losing data. If you’ve backed up your data regularly, you’ll minimize what you lose.

Recover your operating system. To find out how to recover your operating system (like Windows or Mac OS), visit your device manufacturer’s website. Recovering your system typically means you’ll get back a lot of the data stored on the device, so it’s a good alternative to reinstalling your operating system (step 6). That is, if it clears the malware problem. After recovering your operating system, you’ll want to go back to steps 2, 3 and 4 to ensure that you’ve removed the malware.
Reinstall your operating system. To find out how to reinstall your operating system (like Windows or Mac OS), visit your device manufacturer’s website. Reinstalling your system is the safest way to clean an infected device, but you’ll lose all of the data stored on the device that you haven’t backed up.
""")