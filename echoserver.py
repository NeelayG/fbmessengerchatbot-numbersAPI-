
from flask import Flask,request,jsonify
from werkzeug.datastructures import ImmutableMultiDict
import random
import requests


app=Flask(__name__)
url = "http://numbersapi.com/"
@app.route('/<idx>', methods=['GET'])
def respond(idx):
  #Accept data from query string herew
  data=request.args.to_dict()
  return jsonify({"reply":"Token is bohthard"+idx})

@app.route('/postJson', methods=['POST'])
def postJson():
  data = request.get_json();
  print(data.values())
  return jsonify(data)
#def verify():
 # data=request.data
  #return data

@app.route("/getFact", methods=["POST"])
def getFact():
 req=request.get_json()
 intent = req.get("queryResult").get("intent").get("displayName")
 number = req.get("queryResult").get("parameters").get("number")
 qtype = req.get("queryResult").get("parameters").get("type") 
 if intent=="number":
   if qtype=="random":
       qtype=random.choice(["math","trivia","year"])
   qurl = url+str(int(number))+"/"+qtype+"?json"
   res = requests.get(qurl).json()["text"]
   return jsonify({"fulfillmentText":res})
   print(qurl)    
   
 print(intent,number,qtype)
 return jsonify({"fulfillmentText":"Flask server hit"})

if __name__ == '__main__':
  app.run()
