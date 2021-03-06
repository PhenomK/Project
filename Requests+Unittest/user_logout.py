import requests
import unittest
import re

class Log(unittest.TestCase):
    def test_logout(self):
        url = "http://172.16.52.138"
        url1 = url + "/v2/user/login"
        payload = {'user_slug': 'chrome', 'password': '123456'}
        r1 = requests.request("POST",url1,params = payload).json()
        line0 = str(r1)
        var0 = str(re.findall(r" 'uid': (.+?), ",line0))
        line5 = str(re.sub(r"\W", "", var0))
        #print(line5)
        r2 = requests.request("POST",url1,params = payload)
        line1 = str(r2.cookies)
        #print(line1)
        var1 = str(re.findall(r'S=(.+?) ', line1))
        line2 = str(re.sub(r"\W", "", var1))
        #print(line2)
        var2 = str(re.findall(r'SESS-ID=(.+?) ', line1))
        line3 = str(re.sub(r"\W", "", var2))
        #print(line3)
        var3 = str(re.findall(r'JSESSIONID=(.+?) ', line1))
        line4 = str(re.sub(r"\W", "", var3))
        url2 = url + "/v2/user/logout"
        querystring2 = {"S": line2,"X-LENOVO-SESS-ID":line3,"JSESSIONID":line4}
        response = requests.request("POST", url2, params=querystring2).json()
        #print(response)

        self.assertEquals(response['uid'], 72 )
if __name__ == '__main__':
    unittest.main()


