from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=064400&page=1" # LG씨엔에스로 원복 사유: 속도때문
response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
source = response.text
#print(source)

#(1) 오늘의 종가를 가져와 보기 ( 우측마우스 -> 검사 -> Copy -> Copy Selector )
#body > table.type2 > tbody > tr:nth-child(3) > td:nth-child(2) > span.tah p11
soup = BeautifulSoup(source, 'lxml')
span_today = soup.find('span', class_="tah p11")
#print(span_today) #<span class="tah p11">256,500</span>
print('#오늘의 종가:', span_today.text) #256,500

#(2) 마지막 페이지숫자 가져오기
#body > table.Nnavi > tbody > tr > td.pgRR > a
td_pgRR = soup.find('td', class_="pgRR")
#print(td_pgRR) #td태그 포함
#print(td_pgRR.text) #'맨뒤'
a_href = td_pgRR.a['href']
#print(a_href) #/item/sise_day.nhn?code=005930&page=755
a_href_split_list = a_href.split('=')
#print(a_href_split_list) #['/item/sise_day.nhn?code', '005930&page', '755']
last_page = a_href_split_list[-1]
print('#마지막 페이지:', last_page) #755

#(3) 전체페이지 읽어오기
import pandas as pd
from io import StringIO
df = pd.DataFrame()
base_url = "https://finance.naver.com/item/sise_day.nhn?code=000660"   # 하이닉스 000660 BY chunseok 수정, LG씨엔에스 064400
for page in range(1, int(last_page)+1):
    url= f'{base_url}&page={page}'
    #print(url)
    response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    #print(source)
    html = pd.read_html(StringIO(source), header=0)[0] #header는 컬럼이름 지정
    #print(html)
    df = pd.concat([df, html], ignore_index=True)
#print(df)

#(4) DataFrame 가공
print('#사이즈(1)', len(df))
df = df.dropna() #빈 행 제거
#print(df)
print('#사이즈(2)',len(df))

df = df.iloc[0:20] #1행 n행까지의 row만 가져옴
#print(df)
df = df.sort_values(by='날짜', ascending=True) #날짜의 오름차순
print(df)

#(5) 차트 그리기
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager
font_path = r"C:\Windows\Fonts\malgun.ttf"
if not os.path.exists(font_path):
    raise FileNotFoundError(f"폰트 파일이 없습니다: {font_path}")
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams["font.family"] = font_name
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지

plt.title('SK하이닉스')  # by chunseok 종목수정 LG씨엔에스에서 SK하이닉스
plt.xticks(rotation=45)
plt.plot(df['날짜'], df['종가'], 'ro-')
plt.grid(color='gray', linestyle="--")

plt.show()


# <0> 종목코드조회
# https://www.ktb.co.kr/trading/popup/itemPop.jspx

# <1> 원하는 종목선택
# https://finance.naver.com/item/sise_day.nhn?code=000660&page=1 #SK하이닉스
# https://finance.naver.com/item/sise_day.nhn?code=005930&page=1 #삼성전자

# <2> 태그추출 (우측마우스 -> 검사 -> Copy -> Copy Selector)
# body > table.type2 > tbody > tr:nth-child(3) > td:nth-child(2) > span.tah p11