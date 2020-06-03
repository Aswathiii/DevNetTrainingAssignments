#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb

cgitb.enable() # Enable debugging
print("Below is the execution output of the script")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######
import requests
import json

def get_file(site2):

    token = get_token()

    url = site2

    payload = {}
    headers = {
        'x-auth-token': token
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    resp1 = response.json()

    #print(resp1)
    return(resp1)
    
import json

def dev_par(site2):
    dev_data = get_file(site2)
    for dnac_device in dev_data['response']:
            print('<br><br>Device ID :', dnac_device['id'])
            print('<br>Device Type :', dnac_device['type'])
            print('<br>Device Family :', dnac_device['family'])
            print('<br>Software Type :', dnac_device['softwareType'])
            print('<br>Management IP Address :', dnac_device['managementIpAddress'])

import requests

def get_token():
    """
    Gets an access token from Cisco DNA Center. Returns the token
    string if successful; raises HTTPError otherwise.
    """

    # Declare useful local variables to simplify request process
    api_path = "https://sandboxdnac2.cisco.com/dna"
    auth = ("dnacdev", "D3v93T@wK!")
    headers = {"Content-Type": "application/json"}

    # Issue HTTP POST request to the proper URL to request a token
    auth_resp = requests.post(
        "{}/system/api/v1/auth/token".format(api_path), auth=auth, headers=headers
    )

    # If successful, print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token


if __name__ =='__main__':
    """
    Execution begins here.
    """

    print("<h3>Printing Token...</h3>")
    token = get_token()
    print("<h3>Token</h3><br><br>{}".format(token) )
    print("<h3>Token printed</h3>")
    # Iterating through all files in data directory:
    print('<br><h1>Device Details : </h1>')
    print('-------------------<br>')
    site2 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'

    dev_par(site2)