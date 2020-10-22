# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:31:07 2020

@author: PREET MODH
"""


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC74b523a2be1ca45cedb6ad493ac2631d"
# Your Auth Token from twilio.com/console
auth_token = '9b2bb7f181c726941213f75b7fba0626'

client = Client(account_sid, auth_token)

for msg in client.messages.list():
    msg.delete()
