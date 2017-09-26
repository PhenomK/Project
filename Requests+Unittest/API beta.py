import requests
import unittest
import re

class Login(unittest.TestCase):
    def test_login(self):
        url = "http://172.16.29.37:8080/v2/user/login"
        querystring = {"user_slug":"chrome","password":"123123"}
        response = requests.request("post", url, params=querystring)
        #print(response.cookies)
    #def test_logout(self):
        url2 = "http://172.16.29.37:8080/v2/user/logout"
        line1 = str(response.cookies)
        var1 = str(re.findall(r'S=(.+?) ',line1))
        line2 =str(re.sub(r"\W","",var1))
        print(line2)
        """
        querystring2 ={"uid":"31","account_id":"1","S":line2}
        print(querystring2)
        response2 = requests.request("POST",url2,params=querystring2).json()
        print(response2)
        """
        url3 = "http://172.16.29.37:8080/v2/user/logout?account_id=1&uid=31&S="+line2
        # line3 = str(url3+line2)
        # print(line3)
        r = requests.post(url3)
        print(r.text)
#    POST http://172.16.29.37:8080/v2/user/logoutr?account_id=1&uid=31&S=5E5D810A

if __name__ == '__main__':
    unittest.main()
