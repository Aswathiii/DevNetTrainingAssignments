import json
import xml.etree.ElementTree as ET
import yaml


def json_parser(json_file):
    with open(json_file, 'r') as f:
        data_json = json.loads(f.read())
        return(data_json)

def xml_parser(xml_file):
    with open(xml_file, 'r') as x:
        tree = ET.parse(x) 
        root = tree.getroot() 
        acnt = {}
        for k in root.iter():
            if ('ACCT' in k.tag):
                at = {}
                for tr in k:
                    at[tr.tag] = tr.text
                acnt[k.tag] = at
    return(acnt)

def yaml_parser(yaml_file):
    with open(yaml_file, 'r') as y:
        data_yaml = yaml.load(y, Loader=yaml.FullLoader)
    return(data_yaml)
