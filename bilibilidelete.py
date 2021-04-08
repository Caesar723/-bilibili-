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
    header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0",
              'cookie': "_uuid=BDF32AB2-B3DC-EC56-963B-C9829A6C30DB06206infoc; buvid3=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; sid=ieln10e8; fingerprint=6de3e7aa3dd941bdb3f87e821df3532d; buvid_fp=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; buvid_fp_plain=3618B6F5-8A0C-42EB-9ACE-091632EC293518565infoc; bp_video_offset_93254219=490725955173595632; bp_t_offset_93254219=491101610196193001; PVID=2; CURRENT_FNVAL=80; blackside_state=1; bsource=search_baidu; DedeUserID=93254219; DedeUserID__ckMd5=147d5c8d721cbde8; SESSDATA=2d7afa93%2C1629878941%2Ca0638*21; bili_jct=a0ecb213fe78518a301baedc8f9b84f9; bfe_id=1bad38f44e358ca77469025e0405c4a6"
              }
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
    header= {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
             'cookie': "_uuid=BDF32AB2-B3DC-EC56-963B-C9829A6C30DB06206infoc; buvid3=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; sid=ieln10e8; fingerprint=c82fe3a536bed28b50b09a0c85f3a5ae; buvid_fp=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; buvid_fp_plain=3709CE82-D37B-44E1-B327-A21981A1D0EB184990infoc; bp_video_offset_93254219=500130932825144632; bp_t_offset_93254219=498942536850901324; PVID=4; CURRENT_FNVAL=80; blackside_state=1; DedeUserID=93254219; DedeUserID__ckMd5=147d5c8d721cbde8; SESSDATA=2d7afa93%2C1629878941%2Ca0638*21; bili_jct=a0ecb213fe78518a301baedc8f9b84f9; rpdid=|(u~||Yu|YYY0J'uYuRRmYlJk; LIVE_BUVID=AUTO4516147624477504; fingerprint3=04ce2257241c7e2a82f1733631579bff; fingerprint_s=627aa720ab7d4d0f05f9c7ea79cf6cee; bfe_id=1bad38f44e358ca77469025e0405c4a6",
             'referer':"https://space.bilibili.com/93254219/fans/follow"
              }
    data = {
        "act": "2",
        "fid": id,
        "re_src": "11",
        "jsonp": "jsonp",
        "csrf": "a0ecb213fe78518a301baedc8f9b84f9"
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

