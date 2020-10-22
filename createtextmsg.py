# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:31:07 2020

@author: PREET MODH
"""


from twilio.rest import Client
account_sid = "YOUR ACCOUNT SID FROM THE WEBSITE"
auth_token = 'YOUR ACCOUNT TOKEN FROM THE WEBSITE'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='THE NUMBER GIVEN FROM TWILIO',
                              body='hello! how r you?',
                              to='THE NUMBER YOU WANT TO SEND MESSAGE'
                          )
print(message.body)
