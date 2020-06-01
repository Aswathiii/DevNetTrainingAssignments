# Import modules
import sys
import json
import xml.etree.ElementTree as ET
import yaml
import os
#import xmltodict
import pprint

# Main function
if __name__ == "__main__":

    print('DevNetAssignment1')

    data_acnt = {}

    #db.json
    with open('data/db.json', 'r') as f:
        data_json = json.loads(f.read())
        data_acnt.update(data_json)

    # db.xml
    with open("data/db.xml", 'r') as x:
        tree = ET.parse(x) 
        root = tree.getroot() 
        acnt = {}
        for k in root.iter():
            if ('ACCT' in k.tag):
                at = {}
                for tr in k:
                    at[tr.tag] = tr.text
                acnt[k.tag] = at
        data_acnt.update(acnt)

    #db.yml
    with open("data/db.yml", 'r') as y:
        data_yaml = yaml.load(y, Loader=yaml.FullLoader)
        data_acnt.update(data_yaml)
    
if __name__ =='__main__':
    # Iterating through all files in data directory:
    print('\nAccount Details : ')
    print('-------------------\n')
    for count in data_acnt:
        print('ACCT NUMBER :', count[4:],"\n")
        print('Paid : ', data_acnt[count]['paid'])
        print('Due : ', data_acnt[count]['due'],"\n")