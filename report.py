import requests
import json

url = 'http://wthrcdn.etouch.cn/weather_mini?city='
city = input('输入城市名获取天气预报\n')
my_url = url+city
try:
	response = requests.get(my_url,timeout = 1)
	f = open('data.txt','w')
	f.write(response.text)
	f.close()
	s = json.loads(response.text)
	print(str(s['data']['city'])+'天气预报')
	for i in range(0,5):
		print(s['data']['forecast'][i]['date'])
		print(s['data']['forecast'][i]['type'])
		print(s['data']['forecast'][i]['high'],s['data']['forecast'][i]['low'])
		print(s['data']['forecast'][i]['fengxiang'])
		print('\n')
	print('友情提示：',s['data']['ganmao'])
except requests.exceptions.RequestException as e:
	print(e)


tmp = input()