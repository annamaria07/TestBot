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
  if data['text'].lower() == "show me the disclamer song please!":
    send_msg("https://youtu.be/ppYYWdQlVNw")


	#Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "sing the disclaimer song":
    send_msg("okie. Hey now, don't try it at home, du du du du. hey now don't try it, don't u dare try it. you might die if you do this at home, du du du- oooo heres the bridge, whoaaa. don't try it. don't do the thing that we're about to doooo. du du du- oh don't try this.. at all or you'll die if.. you try this thing at hoooooome du du du- ooooooooo its a key change, OOOOoooo its a key change, ooooOOOooOOO its the disclaimers sOOOOOOooooong....  don't try this at hoome, if you do you might diie, this is our disclaimer to ya, hey, don't be that guUuy, just watch us do the thing you wanna doooououooo- be safe, fo rme, but be safe, for youuuuu... DU DU DU DU-BA.")

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
