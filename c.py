from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.nate.com/')
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')
#result = soup.select("#olLiveIssueKeyword > li:nth-child(1)") #1번 or 6번
results = soup.select("#olLiveIssueKeyword > li") #<li>의 list 형식
#print(results)

for li in results:
    span = li.select_one('.txt_rank')
    #print(span)

    if span:
        print(span.get_text(strip=True))
