import requests
import json
from bs4 import BeautifulSoup
item_id="DPAI1H-A900AM7E2"
def pchome(item_id):
    p_url="https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id="+item_id+"&fields=Seq,Id,Price,Qty,ButtonType,SaleStatus"
    r = requests.get (p_url)    
    code = json.loads(r.text)
    code = code[0]
    idd = code['Id']
    qty = code['Qty']
    price = code['Price']['P']
    salestatus = code['SaleStatus']
    return price,salestatus

def momo_goods_price(i_code):
    params = {"i_code": i_code}
    response = requests.get("https://m.momoshop.com.tw/goods.momo",
                params=params,
                headers={"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
                        "content-type": "text/html; charset=UTF-8",
                        "referer": "https://m.momoshop.com.tw/"},
                timeout=4,
            )
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')
    a=soup.findAll("li")
    for i in a:
        if i.find('b',class_="price") != None:
            print(i.find('b',class_="price"))
            
            
momo_goods_price("9750948")
