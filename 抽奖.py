from urllib import request, parse
import json
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
def first():

    url="https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_new?topic_id=3230836"
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0"}
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
        "csrf_token": "a0ecb213fe78518a301baedc8f9b84f9",
        "csrf": "a0ecb213fe78518a301baedc8f9b84f9"
    }
    header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0",
              'cookie': "_uuid=BDF32AB2-B3DC-EC56-963B-C9829A6C30DB06206infoc; buvid3=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; sid=ieln10e8; fingerprint=6de3e7aa3dd941bdb3f87e821df3532d; buvid_fp=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; buvid_fp_plain=3618B6F5-8A0C-42EB-9ACE-091632EC293518565infoc; bp_video_offset_93254219=490725955173595632; bp_t_offset_93254219=491101610196193001; PVID=2; CURRENT_FNVAL=80; blackside_state=1; bsource=search_baidu; DedeUserID=93254219; DedeUserID__ckMd5=147d5c8d721cbde8; SESSDATA=2d7afa93%2C1629878941%2Ca0638*21; bili_jct=a0ecb213fe78518a301baedc8f9b84f9; bfe_id=1bad38f44e358ca77469025e0405c4a6",
              'referer': "https://t.bilibili.com/topic/name/%E4%BA%92%E5%8A%A8%E6%8A%BD%E5%A5%96/feed"
              }
    data=parse.urlencode(data).encode("utf-8")
    html=request.Request(url=url,headers=header,data=data,method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)
    print(data)
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
        "csrf_token": "a0ecb213fe78518a301baedc8f9b84f9",
        "csrf": "a0ecb213fe78518a301baedc8f9b84f9"
    }
    data = parse.urlencode(data).encode("utf-8")
    html = request.Request(url=url, headers=header, data=data, method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)
    print(data)
def getdata(num,fir):
    global uid,did,rid,dmn
    url="https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?topic_name=%E4%BA%92%E5%8A%A8%E6%8A%BD%E5%A5%96&offset_dynamic_id="+str(fir)
    header={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0"}
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
    header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0",
              'cookie': "_uuid=BDF32AB2-B3DC-EC56-963B-C9829A6C30DB06206infoc; buvid3=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; sid=ieln10e8; fingerprint=6de3e7aa3dd941bdb3f87e821df3532d; buvid_fp=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; buvid_fp_plain=3618B6F5-8A0C-42EB-9ACE-091632EC293518565infoc; bp_video_offset_93254219=490725955173595632; bp_t_offset_93254219=491101610196193001; PVID=2; CURRENT_FNVAL=80; blackside_state=1; bsource=search_baidu; DedeUserID=93254219; DedeUserID__ckMd5=147d5c8d721cbde8; SESSDATA=2d7afa93%2C1629878941%2Ca0638*21; bili_jct=a0ecb213fe78518a301baedc8f9b84f9; bfe_id=1bad38f44e358ca77469025e0405c4a6",
              'referer': "https://t.bilibili.com/topic/name/%E4%BA%92%E5%8A%A8%E6%8A%BD%E5%A5%96/feed"
              }
    data = {
            'oid':id,
            'type': '11',
            'message': "拉低中奖率",
            'plat': '1',
            'ordering': 'heat',
            'jsonp': 'jsonp',
            'csrf': 'a0ecb213fe78518a301baedc8f9b84f9' #没有过多研究，个人理解为每个用户拥有的验证特征码  需要自行去手动评论F12抓包获取
        }
    data=parse.urlencode(data).encode('utf-8')
    html=request.Request(url=url, headers=header,data=data,method='POST')
    response = request.urlopen(html)


    data = response.read()
    data = json.loads(data)
    error=data["code"]
    print(data)
first=first()
for i in range(0,1000):
    getdata(0,first)
    first=dmn
    comment(rid)

    if error==0:

        attention(uid)
        repost(did)

    time.sleep(15)


