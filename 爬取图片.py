import requests
import os
url = "http://www.maomaogougou.cn/tupian/a0upkv.html"
root = "E://python课后//46爬虫实例//图片//"
path = root + url.split('/')[-1]

try:
    kv = {"user-agent":"Mozilla/5.0"}
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,headers = kv)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("爬取失败")


