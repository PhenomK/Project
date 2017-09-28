import requests
import unittest
import re
import random

class Create_User(unittest.TestCase):
    def test_create(self):
        url = "http://172.16.29.37:8080/v2/user/login"
        querystring = {"user_slug":"admin","password":"123456"}
        response1 = requests.request("post",url,params = querystring)
        response2 = requests.request("post",url,params = querystring).json()
        line0 = str(response1.cookies)
        line1 = str(response2)
        var1 = str(re.findall(r"'uid': (.+?),", line1))
        line2 = str(re.sub(r"\W", "", var1))              # uid
        var2 = str(re.findall(r"'account_id': (.+?),", line1))
        line3 = str(re.sub(r"\W", "", var2))              # account_id
        var3 = str(re.findall(r'S=(.+?) ', line0))
        line4 = str(re.sub(r"\W", "", var3))              # S
        var4 = str(re.findall(r'SESS-ID=(.+?) ', line0))
        line5 = str(re.sub(r"\W", "", var4))              # SESS-ID
        var5 = str(re.findall(r'JSESSIONID=(.+?) ', line0))
        line6 = str(re.sub(r"\W", "", var5))              # JSESSIONID
        i = str(random.randint(0, 1000))
        url2 = "http://172.16.29.37:8080/v2/notice/create"
        querystring2 = {"account_id": line3,
                        "uid": line2,
                        "S": line4,
                        "X-LENOVO-SESS-ID": line5,
                        "JSESSIONID": line6,
                        "title":"Notice title"+ i ,
                        "body":"Notice body"+ i }
        response3 = requests.request("POST",url2, params=querystring2).json()
        #print(response3)
        self.assertRegexpMatches(response3['title'], 'Notice title' + i)
        self.assertRegexpMatches(response3['body'], 'Notice body' + i)
if __name__ == '__main__':
    unittest.main()