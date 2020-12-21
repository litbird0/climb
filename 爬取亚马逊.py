import requests
url = "https://www.amazon.cn/deal/742bec77/ref=gbph_img_d-2_0947_742bec77?marketplaceId=AAHKV2X7AFYLW&showVariations=false&smid=A3TEGLC21NOO5Y&pf_rd_p=28b2d4cd-6ae8-42c8-8eee-c98227ec0947&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=TKA64CCWYDY3SXWVSCG8"

try:
    kv = {'user-agent':'Mozilla/5.0'}  #重新定义头部信息中的user-agent的内容
                                    # 'Mozilla/5.0':说明这次访问可能是浏览器

    r = requests.get(url, headers = kv)  #获取网页
    print(r.status_code)   #获取状态码：正确为200，不是200都是爬取失败
    print(r.encoding)      #获取头部的编码
    print(r.apparent_encoding)   #获取内容的编码
    print(r.text)                #根据encoding的编码转换成的字符串
    print(r.request.headers)     #获取头部信息
except:
    print("爬取失败")
