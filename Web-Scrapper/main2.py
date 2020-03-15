# %%
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
url = "https://store.musinsa.com/app/product/search?chk_research=&q=%EB%AC%B4%EC%8B%A0%EC%82%AC%20%EC%8A%A4%ED%83%A0%EB%8B%A4%EB%93%9C"
# %%


def get_last_page(soup):
    musinsa = requests.get(url)
    soup = BeautifulSoup(musinsa.text, features='html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    pages = pagination.find_all('a', {"class": "btn"})
    last_page_hint = pages[-1]["onclick"]
    last_page_hint = str(last_page_hint)
    last_page_hint2 = re.search(r"f1,\s\D\d*", last_page_hint).group()
    last_page = re.search(r"\d*$", last_page_hint2).group()
    return int(last_page)
# %%


def get_items(li):
    item_name = li.find('p', {"class": "list_info"})
    return item_name.find("a")['title']
# %%


def get_price(li):
    item_prices = li.find('p', {'class': "price"})
    discount_price = re.search(
        r'\d*\D*\d*\D$', item_prices.get_text(strip=True))
    return discount_price.group()

# %%


def get_comment_count(li):
    com_count = li.find("span", {"class": "count"})
    if com_count != None:
        return str(com_count.string)
    else:
        return '0'

# %%


def get_love_count(li):
    love_count = li.find('p', {"class": "txt_cnt_like"})
    if love_count != None:
        return love_count.get_text(strip=True)
    else:
        return '0'
# %%


def get_link(li):
    link_num = li.a['href']
    link = f"https://store.musinsa.com{link_num}"
    return link

# %%


def get_info(li):
    item_name = get_items(li)
    price = get_price(li)
    comment_count = get_comment_count(li)
    love_count = get_love_count(li)
    link = get_link(li)
    return {"item": item_name, "price": price, "comment_count": comment_count, "love_count": love_count, "link": link}
# %%


def get_total_info(last_page):
    total_info = []
    url = "https://store.musinsa.com/app/product/search?chk_research=&q=%EB%AC%B4%EC%8B%A0%EC%82%AC%20%EC%8A%A4%ED%83%A0%EB%8B%A4%EB%93%9C"
    for page in range(last_page):
        print(f"Scrapping {page+1}")
        url = f"{url}&sort=pop&page={page+1}"
        musinsa = requests.get(url)
        soup = BeautifulSoup(musinsa.text, features='html.parser')
        lists = soup.find_all("div", {"class": "li_inner"})
        for li in lists:
            info = get_info(li)
            total_info.append(info)
    return total_info

# %%


def Excute():
    musinsa = requests.get(url)
    soup = BeautifulSoup(musinsa.text, features='html.parser')
    last_page = get_last_page(soup)
    return get_total_info(last_page)


# %%
musinsa_standard_file = Excute()
print(musinsa_standard_file)
# %%
save_path = "musinsa.csv"
musinsa_df = pd.DataFrame(musinsa_standard_file)
musinsa_df.to_csv(save_path)
# %%
