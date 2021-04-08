from urllib import request, parse
import json
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
csrf=1
def first():

    url="https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_new?topic_id=3230836"
    header = {"User-Agent": ""}
    html = request.Request(url=url, headers=header)
    html = request.urlopen(html)
    html = json.loads(html.read())
    first=html["data"]["offset"]
    return first
def attention(id):
    global header
    url="https://api.bilibili.com/x/relation/modify"
    data={
        "act": "1",
        "fid": id,
        "spmid": "333.169",
        "re_src": "0",
        "csrf_token": "",
        "csrf": ""
    }
    header = {'user-agent': "",
              'cookie': "", 'referer': "https://t.bilibili.com/topic/name/%E4%BA%92%E5%8A%A8%E6%8A%BD%E5%A5%96/feed"
              }
    data=parse.urlencode(data).encode("utf-8")
    html=request.Request(url=url,headers=header,data=data,method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)

def repost(dn):
    global header
    url="https://api.vc.bilibili.com/dynamic_repost/v1/dynamic_repost/repost"
    header=header
    data={
        "uid": "93254219",
        "dynamic_id": dn,
        "content": "拉低中奖率",
        "extension": "{\"emoji_type\":1}",
        "at_uids": "",
        "ctrl": "[]",
        "csrf_token": "",
        "csrf": ""
    }
    data = parse.urlencode(data).encode("utf-8")
    html = request.Request(url=url, headers=header, data=data, method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)

def getdata(num,fir):
    global uid,did,rid,dmn
    url="https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?topic_name=%E4%BA%92%E5%8A%A8%E6%8A%BD%E5%A5%96&offset_dynamic_id="+str(fir)
    header={ "User-Agent": ""}
    html=request.Request(url=url,headers=header)
    html=request.urlopen(html)
    html=json.loads(html.read())
    into=html["data"]["cards"][num]["desc"]
    uid=into["uid"]
    did=into["dynamic_id"]
    rid=into["rid"]
    dmn=into["dynamic_id"]
def comment(id):
    global error
    url = 'https://api.bilibili.com/x/v2/reply/add'
    header = {'user-agent': "",
              'cookie': "",  'referer': "https://t.bilibili.com/topic/name/%E4%BA%92%E5%8A%A8%E6%8A%BD%E5%A5%96/feed"#cookie uesr agent 用自己的
              }
    data = {
            'oid':id,
            'type': '11',
            'message': "拉低中奖率",
            'plat': '1',
            'ordering': 'heat',
            'jsonp': 'jsonp',
            'csrf': '' #没有过多研究，个人理解为每个用户拥有的验证特征码  需要自行去手动评论F12抓包获取
        }
    data=parse.urlencode(data).encode('utf-8')
    html=request.Request(url=url, headers=header,data=data,method='POST')
    response = request.urlopen(html)


    data = response.read()
    data = json.loads(data)
    error=data["code"]
count=0
first=first()
for i in range(0,2000):
    getdata(0,first)
    first=dmn
    comment(rid)

    if error==0:
        count+=1
        attention(uid)
        repost(did)
        print("发送成功，已发送："+str(count))
    time.sleep(15)


