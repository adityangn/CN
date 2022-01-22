# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:07:23 2021

@author: Aditya Navin Nair and Ashwin MS
"""

import socket

run_client = True
while run_client:
    c=socket.socket()
    c.connect(('localhost',9999))
    str=input('Enter command: ')
    c.send(bytes(str,'utf-8'))
    print(c.recv(1024).decode())
    c.close()
    choice = input("Enter 'yes' to continue or 'no' to stop client: ")
    if choice == 'yes':
        run_client = True
    else:
        run_client = False


