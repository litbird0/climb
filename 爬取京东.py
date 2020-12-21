import requests
url = "https://item.jd.com/100008045212.html"
try:
    r = requests.get(url)
    print(r.status_code)
    r.raise_for_status()
    print(r.encoding)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
