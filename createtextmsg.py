# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:31:07 2020

@author: PREET MODH
"""


from twilio.rest import Client
account_sid = "AC74b523a2be1ca45cedb6ad493ac2631d"
auth_token = '9b2bb7f181c726941213f75b7fba0626'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12058595019',
                              body='hello! how r you?',
                              to='+919428132069'
                          )
print(message.body)