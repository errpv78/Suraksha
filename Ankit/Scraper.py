# Scraping News
import html
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

urlList = ['https://economictimes.indiatimes.com/topic/women/news']
headlines = []
newsSummary = []
newsBody = []
baseURL = 'https://economictimes.indiatimes.com'

for url in urlList:
     
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage,"html.parser")
    
    # fetching links of articles on Home page
    divTag = page_soup.find_all('div', class_= 'flr topicstry')
    
    links = []
    for tag in divTag:
        tdTags = tag.find("a")
        if tdTags == None:
            continue
        links.append(tdTags.get("href"))
        
    divTag = page_soup.find_all('div', class_= 'clr flt topicstry')
    
    for tag in divTag:
        tdTags = tag.find("a")
        if tdTags == None:
            continue
        links.append(tdTags.get("href"))
        
    # fetching headline, summary and news of homepage news
    for link in links:
        cur_url = baseURL+link
        # print(cur_url)
        news_req = Request(cur_url, headers={'User-Agent':'Mozilla/5.0'})
        news_webpage = urlopen(news_req).read()
        news_page_soup = soup(news_webpage,"html.parser")
        
        article_title = news_page_soup.find('h1', class_ ='clearfix title')
        headlines.append(article_title.text)
        # print(article_title.text)
        
        article_summary = news_page_soup.find('h2', class_ ='title2')
        newsSummary.append(article_summary.text)
        
        article_body = news_page_soup.find('div', class_ ='Normal')
        newsBody.append(article_body.text)

# Print headlines, newsSummary and newsBody to see them
