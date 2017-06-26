# -*- coding: utf-8 -*-

import requests
import json

class newAPI():
    conf={
    "username":"***",
    "password":"***",
    "login_url":"http://dev.laohu.com/pack/login",
    "getlist_url":"http://dev.laohu.com/pack/sdklist",
    "get_channel_packfile_url":"http://dev.laohu.com/pack/get_channel_packfilelist",
    "get_common_packfile_url":"http://dev.laohu.com/pack/get_common_packfilelist",
    "check_update_url":"http://dev.laohu.com/pack/latest_client_version",
    }
    def login_token(self):
        postdata={
            'userName':'*@*.*',
            'password':'****'
        }
        res=requests.post(url=newAPI.conf['login_url'],data=postdata)
        code=json.loads(res.text)['code']
        if code==0:
            return json.loads(res.text)['data']['token']
        else:
            return NULL
    def get_list(self):
        typedata={
            'platType':'android'
        }
        try:
            listres=requests.post(url=newAPI.conf['getlist_url'],data=typedata)
        except:
            print "post data error"
        listtext=json.loads(listres.text)
        if listtext['code']!=0:
            print "error,code is %s"  % listtext['code']
        else:
            list=listtext['data']
            return list



