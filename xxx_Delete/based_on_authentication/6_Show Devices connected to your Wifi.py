import streamlit as lit
import Scanners.ipscan
import subprocess


lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")

# -- Navigation bar
lit.markdown("# Show Devices ")

lit.write ("The scan starts automatically and will take a few minutes to gather the information.")

Scanners.ipscan.ipscanner_lit()


# output = subprocess.check_output(("arp", "-a"))

# output_str = output.decode()
# for line in output_str.split('\n'):
#     lit.write(line)
