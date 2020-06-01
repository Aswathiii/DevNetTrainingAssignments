import unittest
import json

from parser import json_parser
from parser import xml_parser
from parser import yaml_parser

class Testing(unittest.TestCase):
    def json_test(self):
        self.assertEqual(json_parser("data/db.json", {'ACCT100': {'paid': 60, 'due': 100}, 'ACCT200': {'paid': 70, 'due': 60}, 'ACCT300': {'paid': 0, 'due': 0}} ))
        
    def xml_test(self):
        self.assertEqual(xml_parser("data/db.xml", {'ACCT400': {'paid': '600', 'due': '10000'}, 'ACCT500': {'paid': '70', 'due': '40'}, 'ACCT600': {'paid': '0', 'due': '0'}}))

    def yml_test(self):
        self.assertEqual(yaml_parser("data/db.yml", {'ACCT700': {'paid': 60, 'due': 100}, 'ACCT800': {'paid': 70, 'due': 60}, 'ACCT900': {'paid': 0, 'due': 0}}))


if __name__ =='__main__':
    unittest.main()