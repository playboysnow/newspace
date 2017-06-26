# -*- coding: utf-8 -*-
import unittest
import requests,re,os
import pandas
import multiprocessing
url='http://104.224.155.241'
URL='http://104.224.155.241/?keyword=123'

def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestwebAPI('test_code'))
    suite.addTest(TestwebAPI('test_redirect'))
    suite.addTest(TestwebAPI('test_skip'))
    return suite
class TestwebAPI(unittest.TestCase):
    def test_code(self):
        response=requests.get(url)
        self.assertEqual(str(response.status_code),'200')
    def test_redirect(self):
        response = requests.get(URL)
        self.assertEqual(str(response.status_code), '200')
    @unittest.skip('don\'t do it now')
    def test_skip(self):
        pass

if __name__=='__main__':
#    unittest.main()
    suite()