import requests
from bs4 import BeautifulSoup

out = open('output.txt', 'w')

for n in range(1, 1000, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=재활용&start=" + str(n),
                       headers={'User-agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    # 반복 : 기사 세부 내용
    # 모든 기사의 제목 출력
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text

        print(title)
        print(title, file=out)



