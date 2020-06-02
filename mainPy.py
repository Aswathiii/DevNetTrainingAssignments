import json
import os

from parser import json_parser
from parser import xml_parser
from parser import yaml_parser


# Main function
if __name__ == "__main__":

    print('DevNetAssignment1')

    data_acnt = {}

    #db.json
    d1 = json_parser("data/db.json")
    data_acnt.update(d1)

    # db.xml
    d2 = xml_parser("data/db.xml")
    data_acnt.update(d2)

    #db.yml
    d3 = yaml_parser("data/db.yml")
    data_acnt.update(d3)
    
    # Iterating through all files in data directory:
    print('\nAccount Details : ')
    print('-------------------\n')
    for count in data_acnt:
        print('ACCT NUMBER :', count[4:],"\n")
        print('Paid : ', data_acnt[count]['paid'])
        print('Due : ', data_acnt[count]['due'],"\n")