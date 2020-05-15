# Scraping toAddress,fromAddress and value
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

links = []
for tag in divTag:
    tdTags = tag.find("a").get('href')
    links.append(tdTags)
    #print(tdTags)

# removing unnecssary links
for link in links:
    if link[0:8]!="/article":
        links.remove(link)

    
# keywords to be used later for finding relevant news
# keywords=['women','Women','woman','Woman','girls','Girls','Girl','girl','rape','Rape','Rapist','rapist']

# fetching headline and news of homepage news
headlines = []
newsBody = []
for link in links:
    cur_url = url[:-1]+link
    #print(cur_url)
    news_req = Request(cur_url, headers={'User-Agent':'Mozilla/5.0'})
    news_webpage = urlopen(news_req).read()
    news_page_soup = soup(news_webpage,"html.parser")
    
    article_title = news_page_soup.find('h1', class_ ='ArticleHeader_headline')
    headlines.append(article_title.text)
    #print(article_title.string)
    
    article_body = news_page_soup.findAll('div', class_ ='StandardArticleBody_body')
    for tag in article_body:
        pTags = tag.find_all("p")
        s=""
        for tag in pTags:
            s=s+(str(tag.text)) + "\n"
        newsBody.append(s)
    
    
