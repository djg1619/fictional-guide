#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#all ports are stated below in a dictionary as a 1:1 value. Some protocols use multiple ports and in these cases the correct answer is the lowest port number.
import random

ports = {'FTP':21,
         'SSH':22,
         'Telnet':23,
         'SMTP':25,
         'DNS':53,
         'HTTP':80,
         'PoP3':110,
         'IMAP':143,
         'HTTPS':443,
         'RDP':3389,
         'NetBIOS':137,
         'SMB':445,
         'SLP':427,
         'AFP':548,
         'DHCP':67,
         'LDAP':389,
         'SNMP':161}

def intro():
    print('Enter the correct port number with the associated protocol, if a protocol uses multiple enter the lowest.')

def quiztime():
    question = random.choice(list(ports))
    print('Enter the port number for: ' + question)
    guess = int(input())
    if guess == ports[question]:
        print('Correct.')
    elif guess != ports[question]:
        print('Incorrect.')

def replay():
    return input('Would you like to play again?: yes or no').lower().startswith('y')

#gameplay loop
intro()
while True:
    quiztime()
    if not replay():
        break


# In[ ]:




