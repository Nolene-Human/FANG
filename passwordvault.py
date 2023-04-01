import streamlit as lit

import random

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lit.write("Generate a random password")
    nr_letters = 5
    nr_symbols = 5
    nr_numbers = 5

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password = []

    while nr_letters > 0:
        pass_lett = random.choice(letters)
        password.append(pass_lett)
        #for password_letter in pass_lett:
        #print(password_letter)
        nr_letters -= 1

    while nr_numbers > 0:
        pass_num = random.choice(numbers)
        password.append(pass_num)
        #for password_numbers in pass_num:
        #print(password_numbers)
        nr_numbers -= 1

    while nr_symbols > 0:
        pass_sym = random.choice(symbols)
        password.append(pass_sym)
        nr_symbols -= 1


    random.shuffle(password)
    lit.write("".join(password))