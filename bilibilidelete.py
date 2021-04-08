from urllib import request, parse
import json
import time
import ssl
run=True
count=0
ssl._create_default_https_context = ssl._create_unverified_context
arr=["天天卡牌","HarV1rS","悠风niu","狂野saiwei","吃節操の萌萌兽w","烛子ikina_光遇","Tomohisa君","花花与三猫CatLive","咩星人的咩星球","最慎重的剁剁","炉石萌萌哒的狗贼","幽灵白的天使"]#在里面输入你不想取关的人
def person(number,ye):
    global name,mid
    url="https://api.bilibili.com/x/relation/followings?vmid=93254219&pn="+str(ye)+"&ps=20"
    header = {'user-agent': "",
              'cookie': ""  }#写自己的
    html = request.Request(url=url, headers=header)
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)
    data=data["data"]["list"][number]
    mid=data["mid"]
    name=data["uname"]
    print(mid,name)
def delete(id):
    url="https://api.bilibili.com/x/relation/modify"
    header= {'user-agent': "",
             'cookie': "",   'referer':"https://space.bilibili.com/93254219/fans/follow"
              }
    data = {
        "act": "2",
        "fid": id,
        "re_src": "11",
        "jsonp": "jsonp",
        "csrf": ""#F12 自己找
    }
    data = parse.urlencode(data).encode("utf-8")
    html=request.Request(url=url, headers=header, data=data, method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)
    print(data)
recode=0
while run:
    test=False
    person(recode,1)
    for i in range(0,len(arr)):
        if arr[i]==name:
            test=True
    if test==True:
        recode+=1
        time.sleep(5)
        continue
    else:
        delete(mid)
    time.sleep(5)

