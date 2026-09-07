from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify()) #계층구조로 html를 보여줌
#print(soup.title)
#print(soup.title.text)
#print(soup.title.parent)
#print(soup.title.parent.name) #head
#print(soup.p)  #첫번째 p
#print(soup.find_all('p')) #p태그들의 list
#print(soup.a) #첫번째 a
#print(soup.find_all('a')) #a태그들의 list
print(soup.get_text()) #태그를 제외한 text들만 출력