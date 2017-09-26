import requests
import unittest
import re
import random

class Create_Folder(unittest.TestCase):
    def test_rename(self):
        url = "http://172.16.29.37:8080/v2/user/login"
        querystring = {"user_slug":"chrome","password":"123123"}
        response = requests.request("post", url, params=querystring)
        line1 = str(response.cookies)
        var1 = str(re.findall(r'S=(.+?) ', line1))
        line2 = str(re.sub(r"\W", "", var1))
        var2 = str(re.findall(r'SESS-ID=(.+?) ', line1))
        line3 = str(re.sub(r"\W", "", var2))
        var3 = str(re.findall(r'JSESSIONID=(.+?) ', line1))
        line4 = str(re.sub(r"\W", "", var3))
        i = str(random.randint(0,1000))
        url2 = "http://172.16.29.37:8080/v2/fileops/create_folder/databox/lenovo"+i
        querystring2 = {"path_type":"self","is_update":"false","account_id":"1","uid":"31","S":line2,"X-LENOVO-SESS-ID":line3,"JSESSIONID":line4}
        response = requests.request("POST", url2, params=querystring2).json()
        #print(response)
        self.assertRegexpMatches(response['result'],'success')
if __name__ == '__main__':
    unittest.main()