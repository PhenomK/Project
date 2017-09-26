import requests
import unittest

class Login(unittest.TestCase):
    def test_login(self):
        url = "http://172.16.29.37:8080/v2/user/login"
        querystring = {"user_slug":"chrome","password":"123123"}
        response = requests.request("post", url, params=querystring).json()
        #print(response)
        self.assertEquals(response['user_name'],'chrome')
        self.assertEquals(response['uid'], 31)
if __name__ == '__main__':
    unittest.main()