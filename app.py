#imports
import os
import sys
import json
import random
import requests
import time
from flask import Flask, request

#define our flask app
app = Flask(__name__)

#Method will automatically execute when our endpoint receives a POST call
@app.route('/', methods=['POST'])
def msg_received_from_group():
  #Format the data we receive as a JSON
  data = request.get_json()
  log('{}'.format(data))
  
  #Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "hi mark!":
    send_msg("hello everybody my name is markiplier")
	
	#Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "whasup":
    send_msg("sup")


	#Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "hey mark":
    send_msg("yeeeees?")


	#Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "sing the disclaimer song":
    send_msg("okie. Hey now, don't try it at home
Do do do do do
Hey now, don't try it
Don't you dare try it
You might die if you do this at home
Do do do do


Oh, here's the bridge, woah
Don't try it
Don't do the thing that we're about to do
Do do do do

Oh, don't try this at all, or you'll die if
You try this thing at home
Do do do do do

OH IT'S A KEY CHANGE!
OH IT'S A KEY CHANGE!
OH IT'S THE DISCLAIMER SONG!

Don't try this at home
If you do, you might die
This is our disclaimer to you
Hey, don't be that guy
Just watch us do the thing you want to
Dooooo
Be safe
For me
But be safe
For you

DO DO DO DO

BAA- ")

  return "ok", 200

 
#Sends a message to the chat that the bot originates from
def send_msg(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  payload = { 'text' : msg, 'bot_id' : '01169029234f8def95b495f31e'}
  r = requests.post(url, data=json.dumps(payload))

#logging function to help debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()
