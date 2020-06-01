import json

def dev_par():
    with open('data/db.json', 'r') as b:
        dev_data = json.load(b)
        final_data = []
        for dnac_device in dev_data['response']:
            t = {}
            t['id'] = dnac_device['id']
            t['family'] = dnac_device['family']
            t['softwareType'] = dnac_device['softwareType']
            t['type'] = dnac_device['type']
            t['managementIpAddress'] = dnac_device['managementIpAddress']
            final_data.append(t)
        return final_data