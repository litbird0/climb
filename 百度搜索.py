import requests

#百度接口： http://www.baidu.com/s?wd:{搜索内容}
#360接口：  http://www.so.com/s?q:{搜索内容}

keyword = 'python'
try:
    kv = {'wd':keyword}
    #kv = {'q':keyword}  # 360搜索
    r = requests.get("http://www.baidu.com/s", params = kv)  #利用params将kv添加进来
    print(r.status_code)
    r.raise_for_status()   #如果状态码不是200，产生异常
    print(r.request.url)   #发给百度的request对应的url
    #http://www.baidu.com/s?wd:python
    #http://www.so.com/s?q:python
    print(len(r.text))
    print(r.text)
except:
    print("爬取异常")
