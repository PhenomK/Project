import requests
import re
url = 'http://172.16.29.37:8080/v2/user/login'
payload = {'user_slug':'chrome','password':'123123'}
r = requests.request('POST',url,params = payload)
print(r)
print(r.cookies)
line1 = str(r.cookies)
var1 = str(re.findall(r'S=(.+?) ',line1))
print(var1)
var2 = re.sub(r"\W","",var1)
print(var2)



