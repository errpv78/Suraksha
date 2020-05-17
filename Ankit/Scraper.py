# Scraping News
import html
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

urlList = ['https://in.reuters.com/','https://in.reuters.com/finance','https://in.reuters.com/finance/economy','https://in.reuters.com/finance/deals','https://in.reuters.com/finance/markets/companyOutlooksNews','https://in.reuters.com/subjects/autos','https://in.reuters.com/news/top-news','https://in.reuters.com/news/south-asia','https://in.reuters.com/news/world','https://in.reuters.com/subjects/special-reports','https://in.reuters.com/subjects/middle-east','https://in.reuters.com/breakingviews','https://in.reuters.com/news/lifestyle','https://in.reuters.com/news/entertainment','https://in.reuters.com/news/oddlyEnough','https://in.reuters.com/news/health','https://in.reuters.com/news/entertainment/arts']
headlines = []
newsBody = []

for url in urlList:
     
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
    
        
       
    # fetching headline and news of homepage news
    for link in links:
        cur_url = urlList[0][:-1]+link
        #print(cur_url)
        news_req = Request(cur_url, headers={'User-Agent':'Mozilla/5.0'})
        news_webpage = urlopen(news_req).read()
        news_page_soup = soup(news_webpage,"html.parser")
        
        article_title = news_page_soup.find('h1', class_ ='ArticleHeader_headline')
        headlines.append(article_title.text)
        print(article_title.text)
        
        article_body = news_page_soup.findAll('div', class_ ='StandardArticleBody_body')
        for tag in article_body:
            pTags = tag.find_all("p")
            s=""
            for tag in pTags:
                s=s+(str(tag.text)) + "\n"
            newsBody.append(s)
            
 # keywords to be used later for finding relevant news
keywords=['women','Women','woman','Woman','girls','Girls','Girl','girl','rape','Rape','Rapist','rapist']

related_news = []
related_title = []

for (i,news) in enumerate(newsBody):
    for x in keywords:
        if x in news:
            related_news.append(news)
            related_title.append(headlines[i])
            break
        

