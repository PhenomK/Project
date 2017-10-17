import requests
import unittest

class Login(unittest.TestCase):
    def test_login(self):
        url = "http://172.16.52.138/v2/user/login"
        querystring = {"user_slug":"chrome","password":"123456"}
        response = requests.request("post", url, params=querystring).json()
        print(response)
        self.assertEquals(response['user_name'],'chrome')
if __name__ == '__main__':
    unittest.main()