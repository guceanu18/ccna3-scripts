import requests
import json
from pprint import pprint

router_csr = {
    "hostname": "192.168.178.147",
    "user": "cisco",
    "pass": "cisco123!",
    "port": "443"
}

url = f"https://{router_csr['hostname']}:{router_csr['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.get(url, headers=headers, auth=(router_csr['user'], router_csr['pass']), verify=False)
api_data = response.json()

pprint(api_data)
print("/" * 20)
print(api_data["ietf-interfaces:interface"]["name"])
print(api_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])
print(api_data["ietf-interfaces:interface"]["description"])
print("/" * 20)

