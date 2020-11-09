import http.client 
import json

conn = http.client.HTTPSConnection("api.gateway.attomdata.com") 

headers = { 
    'accept': "application/json", 
    'apikey': "e92c3c36ed7cfef9c73e0736326281a9", 
} 

radius = 20
conn.request("GET", "/propertyapi/v1.0.0/property/address?address1=7131%20wintery%20loo%5B&address2=COLORADO%20SPRINGS%2C%20CO&radius=1&page=0&pagesize=100", headers=headers) 

res = conn.getresponse() 
data = res.read() 


info = json.loads(data)["property"]

for address in info:
    print("Address: ", address, "\n")
# for thing in info['property']:
#     for fuk in thing:
#         print(fuk, ": ", thing[fuk])
#     print("\n")