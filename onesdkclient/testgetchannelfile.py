# -*- coding : utf-8 -*-
from common import newAPI
import unittest
import requests
import random
import json


class get_channel_file(unittest.TestCase):
    def setUp(self):
        self.token=newAPI().login_token()
        self.data = newAPI().get_list()
        self.randomnum = random.randint(0, len(self.data)-1)
        self.randomdata = self.data[self.randomnum]
        self.postdata = {
            'channelId': self.randomdata['channelId'],
            'platformId': self.randomdata['platformId'],
            'version': self.randomdata['configVersion'],
            'token': self.token
        }
    def tearDown(self):
        self.postdata={ }
    def test_nomral(self):
        res=requests.post(url=newAPI().conf['get_channel_packfile_url'],data=self.postdata)
        code = json.loads(res.text)['code']
        self.assertEqual(str(code), '0')
    def test_token_error(self):
        self.postdata['token']="123"
        res = requests.post(url=newAPI().conf['get_channel_packfile_url'], data=self.postdata)
        #code = json.loads(res.text)['code']
        self.assertEqual(str(res.status_code), '403')
    def test_error_channelId(self):
        self.postdata['channelId'] = len(self.data)
        res = requests.post(url=newAPI().conf['get_channel_packfile_url'], data=self.postdata)
        code = json.loads(res.text)['code']
        self.assertEqual(str(code), '1')
    def test_error_platformId(self):
        self.postdata['platformId'] = len(self.data)+55
        res = requests.post(url=newAPI().conf['get_channel_packfile_url'], data=self.postdata)
        code = json.loads(res.text)['code']
        self.assertEqual(str(code), '1')
    def test_error_version(self):
        self.postdata['version'] = "3.0.20"
        res = requests.post(url=newAPI().conf['get_channel_packfile_url'], data=self.postdata)
        code = json.loads(res.text)['code']
        self.assertEqual(str(code), '1')
    def test_empty_param(self):
        param=['channelId','platformId','version']
        param_nu=random.randint(0,len(param)-1)
        self.postdata[param[param_nu]]=" "
        res = requests.post(url=newAPI().conf['get_channel_packfile_url'], data=self.postdata)
        code = json.loads(res.text)['code']
        self.assertEqual(str(code), '1')

if __name__=='__main__':
    case = unittest.TestLoader().loadTestsFromTestCase(get_channel_file)
    unittest.TextTestRunner(verbosity=2).run(case)




