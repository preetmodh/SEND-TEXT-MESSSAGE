# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:31:07 2020

@author: PREET MODH
"""


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "YOUR ACCOUNT SID FROM THE WEBSITE"
# Your Auth Token from twilio.com/console
account_sid = "YOUR ACCOUNT SID FROM THE WEBSITE"

client = Client(account_sid, auth_token)

for msg in client.messages.list():
    msg.delete()

    
    
    
   
