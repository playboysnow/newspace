# -*- coding : utf-8 -*-
import requests
import json
import unittest
from common import newAPI

class  get_commonfile(unittest.TestCase):
    def setUp(self):
        self.token = {
            'token': newAPI().login_token()
        }

    def tearDown(self):
        self.token = {}
    def test_normal(self):
        res=requests.post(url=newAPI().conf['get_common_packfile_url'],data=self.token)
        code=json.loads(res.text)['code']
        self.assertEqual(str(code),'0')
    def test_error(self):
        self.token['token']="123"
        res=requests.post(url=newAPI().conf['get_common_packfile_url'],data=self.token)
        self.assertEqual(str(res.status_code),'403')
    def test_empty(self):
        self.token['token']=" "
        res=requests.post(url=newAPI().conf['get_common_packfile_url'],data=self.token)
        self.assertEqual(str(res.status_code),'403')

if __name__=='__main__':
    case = unittest.TestLoader().loadTestsFromTestCase(get_commonfile)
    unittest.TextTestRunner(verbosity=2).run(case)
