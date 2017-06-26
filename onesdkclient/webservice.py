import urllib,urllib2

def post(url,data):
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response=opener.open(req,data)

    return response.read()


if __name__=='__main__':
    url="http://127.0.0.1/DVWA/login.php"
    data={'username':'admin','password':'password','Login':'Login'}
    post(url,data)