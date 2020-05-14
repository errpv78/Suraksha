import html
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

url = 'https://in.reuters.com/' 
 
req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage,"html.parser")
#print(page_soup)

# fetching links of articles on Home page
divTag = page_soup.find_all('div', class_= 'story-content')

for tag in divTag:
    tdTags = tag.find("a").get('href')
    links.append(tdTags)
    #print(tdTags)

links =[]
for link in page_soup.findAll('a'):
    links.append(link.get('href'))
    
# keywords to be used later for finding relevant news
# keywords=['women','Women','woman','Woman','girls','Girls','Girl','girl','rape','Rape','Rapist','rapist']

# fetching headline and news of homepage news
headlines = []
for link in links:
    cur_url = url[:-1]+link
    news_req = Request(cur_url, headers={'User-Agent':'Mozilla/5.0'})
    news_webpage = urlopen(news_req).read()
    news_page_soup = soup(news_webpage,"html.parser")
    article_title = news_page_soup.find('h1', class_ ='ArticleHeader_headline')
    headlines.append(article_title.string)
    #print(article_title.string)
