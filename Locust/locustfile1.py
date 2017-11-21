from locust import HttpLocust, TaskSet, task
import random
import re
import requests

# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def create(self):
        url = "http://172.16.52.58"
        url1 = url + "/v2/user/login"
        querystring = {"user_slug": "chrome", "password": "123456"}
        response1 = requests.request("post", url1, params=querystring)
        response2 = requests.request("post", url1, params=querystring).json()
        print(response2)
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
        #i = str(random.randint(0, 10000000000))
        url = "/v2/files/databox/lenovo.pdf"
        self.client.post(url ,{"path_type": "self","overwrite":"true", "source": "file","account_id":line3, "uid": line2, "S": line4,"X-LENOVO-SESS-ID": line5, "JSESSIONID": line6})



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000