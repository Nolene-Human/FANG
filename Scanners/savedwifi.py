# importing subprocess
import subprocess

output = subprocess.check_output(("arp", "-a"))


def networkdevices():
    # getting meta data of the wifi network
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    
    # decoding meta data from byte to string
    data = meta_data.decode('utf-8', errors ="backslashreplace")
    
    # splitting data by line by line
    # string to list
    data = data.split('\n')
    
    # creating a list of wifi names
    names = []
    
    # traverse the list
    for i in data:
        
        # find "All User Profile" in each item
        # as this item will have the wifi name
        if "All User Profile" in i :
            
            # if found split the item
            # in order to get only the name
            i = i.split(":")
            
            # item at index 1 will be the wifi name
            i = i[1]
            
            # formatting the name
            # first and last character is use less
            i = i[1:-1]
            
            # appending the wifi name in the list
            names.append(i)
    
    # printing the wifi names
    print("All wifi's your device ever connected to are ")
    print("-----------------------------------------")
    for name in names:
        print(name)

    print(output)

        # st.write("Here's our first attempt at using data to create a table:")
#st.write(pd.DataFrame({
    #'first column': [1, 2, 3, 4],
    #'second column': [10, 20, 30, 40]
#}))