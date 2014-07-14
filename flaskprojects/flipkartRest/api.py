from flask import Flask,jsonify
import requests
import simplejson 
import json

app = Flask(__name__)

@app.route("/")
def home():
    uri = "https://affiliate-api.flipkart.net/affiliate/feeds/rajeshsmu/category/v1:tyy-4io.json?expiresAt=1404918735651&sig=89bf16d26fde155ff29db99893ea3b09"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    productId = data['productId'][0]['display_id']# <-- The display name
    title = data['title'][0]['reputation']# <-- The reputation

    return Jresponse

if __name__ == "__main__":
    app.run(debug = True)