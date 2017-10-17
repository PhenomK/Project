import requests
import unittest
import re
import random

class Create_User(unittest.TestCase):
    def test_create(self):
        url = "http://172.16.52.138/v2/user/login"
        querystring = {"user_slug":"admin","password":"123456"}
        response1 = requests.request("post", url, params=querystring)
        response2 = requests.request("post", url, params=querystring).json()
        #print(response2)
        line0 = str(response1.cookies)
        line1 = str(response2)                              # body
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
        url2 = "http://172.16.52.138/v2/user/create"
        querystring2 = {"user_name": "lenovo"+i,        #用户名
                        "user_slug": "lenovo"+i,        #登录名
                        "password":"123456",            #密码
                        "email":"lenovo@lenovocloud.com"+i,         #邮箱
                        "quota":"1073741824",           #本地空间大小1G
                        "use_local_quota":"1",          #开启本地空间
                        "use_cloud_quota":"1",          #开启云端空间
                        "cloud_quota":"1073741824",    #云端空间大小1G
                        "cloud_allow_scan":"1",         #开启企业空间
                        "use_threshold":"0",            #不限速
                        "active":"true",                 #不冻结用户
                        "account_id": line3,
                        "uid": line2,
                        "S": line4,
                        "X-LENOVO-SESS-ID": line5,
                        "JSESSIONID": line6}
        response3 = requests.request("POST", url2, params=querystring2).json()
        #print(response3)
        self.assertRegexpMatches(response3['user_slug'], 'lenovo'+ i )
        self.assertRegexpMatches(response3['user_name'], 'lenovo'+ i )
        self.assertRegexpMatches(response3['email'], 'lenovo@lenovocloud.com' + i )
if __name__ == '__main__':
    unittest.main()



