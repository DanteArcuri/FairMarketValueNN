import http.client 
from flask import render_template, url_for, Response, request, redirect, session
import requests
import json
import os
import time
from app import app

conn = http.client.HTTPSConnection("api.gateway.attomdata.com") 

headers = { 
    'accept': "application/json", 
    'apikey': "e92c3c36ed7cfef9c73e0736326281a9", 
} 

radius = 20

@app.route('/home', methods=["GET"])
def home():
    conn.request("GET", "/propertyapi/v1.0.0/property/address?address1=31%20wintery%20loo%5B&address2=COLORADO%20SPRINGS%2C%20CO&radius=1&page=0&pagesize=100", headers=headers) 

    res = conn.getresponse() 
    data = res.read() 


    info = json.loads(data)
    print(info['status'])
    return render_template('home.html', housingData=info)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081)