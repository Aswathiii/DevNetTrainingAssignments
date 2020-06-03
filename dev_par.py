import json
from parser import json_parser
from index import get_file

def dev_par(site2):
    dev_data = get_file(site2)
    for dnac_device in dev_data['response']:
            print('<h2>\nDevice ID :</h2>', dnac_device['id'])
            print('<h2>Device Type :</h2>', dnac_device['type'])
            print('<h2>Device Family :</h2>', dnac_device['family'])
            print('<h2>Software Type :</h2>', dnac_device['softwareType'])
            print('<h2>Management IP Address :</h2>', dnac_device['managementIpAddress'],'\n')


if __name__ =='__main__':
    # Iterating through all files in data directory:
    print('\<h1>nDevice Details : </h1>')
    print('<h1>-------------------\n</h1>')
    site2 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'

    dev_par(site2)