import json
from parser import json_parser

def dev_par(file_dev):
    with open(file_dev, 'r') as b:
        dev_data = json.load(b)
        for dnac_device in dev_data['response']:
            print('Device ID :', dnac_device['id'])
            print('Device Type :', dnac_device['type'])
            print('Device Family :', dnac_device['family'])
            print('Software Type :', dnac_device['softwareType'])
            print('Management IP Address :', dnac_device['managementIpAddress'],'\n')


if __name__ =='__main__':
    # Iterating through all files in data directory:
    print('\nDevice Details : ')
    print('-------------------\n')
    dev_par('data/dnac_devices.json')