from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import chat, Group

def home(request):
    topics = []
    href = []
    a = 0
    topics_url = 'https://www.ndtv.com/'
    response1 = requests.get(topics_url)
    response1.status_code
    page_content = response1.text
    doc1 = BeautifulSoup(page_content, 'html.parser')
    selection_class1 = 'item-title'
    title_tags = doc1.find_all('a',{'class':selection_class1})
    for title in title_tags[:4]:
        topics.append(title.text)
        href.append(str(a))
        a += 1
    all = zip(topics,href)
    print(all)
    return render(request, 'app/home.html',{'topics':topics, 'all':all})


def news(request,i):
    group = Group.objects.filter(name = str(i)).first()
    chats = []
    if group:
        chats=chat.objects.filter(group=group)
    else:
        group = Group(name = str(i))
        group.save()
    contents = []
    topics_url = 'https://www.ndtv.com/'
    response1 = requests.get(topics_url)
    page_content = response1.text
    doc1 = BeautifulSoup(page_content, 'html.parser')
    selection_class1 = 'item-title'
    title_tags = doc1.find_all('a',{'class':selection_class1})
    topics_desc_url = title_tags[i]['href']
    response2 = requests.get(topics_desc_url)
    response2.status_code
    page_desc_content = response2.text
    doc2 = BeautifulSoup(page_desc_content, 'html.parser')
    selection_class2 = 'sp-cn ins_storybody'
    items = doc2.find_all("div", {"class":selection_class2})
    try:
        images = items[0].find_all("div", {"class":'ins_instory_dv_cont'})
        imageSources = images[0].findChildren("img")
        source = imageSources[0].get('src')
        print(imageSources[0].get('src'))
    except Exception as e:
        print(e)
        source = 'None'
    for item in items:
        titles = item.find_all("p")
        for title in titles:
            contents.append(title.text)
    return render(request, 'app/news.html',{'contents':contents, 'title':title_tags[i].text, 'source':source, 'i':str(i), 'chats':chats})
