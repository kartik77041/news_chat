import requests
from bs4 import BeautifulSoup
topics_url = 'https://www.ndtv.com/'
response1 = requests.get(topics_url)
response1.status_code
# print(len(response.text))
page_content = response1.text
doc1 = BeautifulSoup(page_content, 'html.parser')
selection_class1 = 'item-title'
title_tags = doc1.find_all('a',{'class':selection_class1})
for title in title_tags[:4]:
    print(title)

# topics_desc_url = title_tags[1]['href']
# # print(topics_desc_url)
# response2 = requests.get(topics_desc_url)
# response2.status_code
# page_desc_content = response2.text
# doc2 = BeautifulSoup(page_desc_content, 'html.parser')
# selection_class2 = 'sp-cn ins_storybody'
# # title_desc_tags = doc2.find_all('p')
# # print(title_desc_tags)
# items = doc2.find_all("div", {"class":selection_class2})
# # for item in items:
# #     titles = item.find_all("p")
# #     for title in titles:
# #         print(title.text)
# images = items[0].find_all("div", {"class":'ins_instory_dv_cont'})
# imageSources = images[0].findChildren("img")
# print(imageSources[0].get('src'))
# # print(imageSources[0])
# # print(imageSources[0].get('integrity'))