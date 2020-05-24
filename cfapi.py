
import urllib.request, urllib.error, urllib.parse
import json
import time
tit=time.time()


req = urllib.request.Request("https://codeforces.com/api/contest.list?gym=false")
response = urllib.request.urlopen(req)


obj = json.loads(response.read())

obj=obj['result']

y=[]
for x in obj:
 if(x['startTimeSeconds']>tit):
     x['startTimeSeconds'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x['startTimeSeconds']))
     y.append(x)
for z in y:
 print(z['name']," | ","Start time  : ",z['startTimeSeconds'])

