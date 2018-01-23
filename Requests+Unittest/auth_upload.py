import requests
import unittest
import re
import random

class Create_Files(unittest.TestCase):
    def test_upload(self):
        url = "http://172.16.52.138"
        url1 = url + "/v2/user/login"
        querystring = {"user_slug":"chrome","password":"123456"}
        response1 = requests.request("post", url1, params=querystring)
        response2 = requests.request("post", url1, params=querystring).json()
        #print(response2)
        line0 = str(response1.cookies)
        line1 = str(response2)  # body
        var1 = str(re.findall(r"'uid': (.+?),", line1))
        line2 = str(re.sub(r"\W", "", var1))  # uid
        var2 = str(re.findall(r"'account_id': (.+?),", line1))
        line3 = str(re.sub(r"\W", "", var2))  # account_id
        var3 = str(re.findall(r'S=(.+?) ', line0))
        line4 = str(re.sub(r"\W", "", var3))  # S
        var4 = str(re.findall(r'SESS-ID=(.+?) ', line0))
        line5 = str(re.sub(r"\W", "", var4))  # SESS-ID
        var5 = str(re.findall(r'JSESSIONID=(.+?) ', line0))
        line6 = str(re.sub(r"\W", "", var5))  # JSESSIONID
        i = str(random.randint(0, 1000))
        url2 = url +"/v2/fileops/auth_upload/databox/lenovo"+ i +".docx"
        querystring2 = {"path_type":"self","file_type":"docx","bytes":"0","is_file_create":"true",
                        "account_id": line3, "uid": line2, "S": line4,"X-LENOVO-SESS-ID": line5, "JSESSIONID": line6}
        response3 = requests.request("GET", url2, params=querystring2).json()
        #print(response3)


        self.assertRegexpMatches(response3['result'],'success')
if __name__ == '__main__':
    unittest.main()

