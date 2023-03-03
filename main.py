import requests
import json
from bs4 import BeautifulSoup

def pchome_goods_price(item_id):
    p_url="https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id="+item_id+"&fields=Seq,Id,Price,Qty,ButtonType,SaleStatus"
    try:
        r = requests.get (p_url)
    except:
        print(f"商品id {item_id} 錯誤")
        return 0     
    code = json.loads(r.text)
    code = code[0]
    idd = code['Id']
    qty = code['Qty']
    price = code['Price']['P']
    salestatus = code['SaleStatus']
    return price

def momo_goods_price(i_code):
    params = {"i_code": i_code}
    try:
        response = requests.get("https://m.momoshop.com.tw/goods.momo",
                    params=params,
                    headers={"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
                            "content-type": "text/html; charset=UTF-8",
                            "referer": "https://m.momoshop.com.tw/"},
                    timeout=4,
                )
        result = response.text
    except:
        print(f"error 商品id {i_code} 錯誤")
        return 0
    
    soup = BeautifulSoup(result, 'html.parser')
    a=soup.findAll("li")
    list=[]
    for i in a:
        if i.find('b',class_="price") != None:
            list.append(i.find('b',class_="price").contents[0])
            print(i.find('b',class_="price").contents[0])
    return list
'''
#範例momo
momo_goods_price("9750948")

#範例pchome
pchome_goods_price("DSABKB-A900FXVUZ")

'''
