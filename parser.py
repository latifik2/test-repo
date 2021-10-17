import requests
from bs4 import BeautifulSoup as BS
from requests.api import request

s = input("Type searching info: \n")
def urlEncode(url):
    url = url.strip().split(" ")
    return ("+").join(url)



s = urlEncode(s)
_request = requests.get("https://www.rusprofile.ru/search?query=" + s + "&type=ul")
html = BS(_request.content, 'html.parser')

#numberOfElems = html.select("search-result-paging hide-mobile > page-navigation > page-nav > page-navigation__num")
#tmp = numberOfElems[1].text.strip().split()
#numberOfPages = int(tmp[1]) // 100
#print(numberOfPages + "\n")

for i in html.select(".search-result__list > .company-item"):
    check = i.select(".company-item-status") 
    #if(check[0].text == "Организация ликвидирована"):
    #    continue

    title = i.select(".company-item__title")
    info = i.select(".company-item-info")
    print(title[0].text.strip() + "\n")
    print(info[0].text.strip()+ "\n")
    print("--------------------------------------------------------------------------------------------------------\n")
