from konlpy.tag import Okt
from collections import Counter

filename = "output_environment.txt"
f = open(filename, 'r', encoding='utf-8')
news = f.read()

# okt 객체 생성
okt = Okt()
noun = okt.nouns(news)
for i, v in enumerate(noun):
    if len(v) < 2:
        noun.pop(i)

count = Counter(noun)
f.close()

# 명사 빈도 카운트
noun_list = count.most_common(100)
for v in noun_list:
    print(v)

# txt 파일에 저장
with open('noun_list.txt', 'w', encoding='utf-8') as f:
    for v in noun_list:
        f.write(" ".join(map(str, v))) # 튜플 int값을 str로 전환 후 조인
        f.write("\n")

# csv 파일에 저장
with open("noun_list.csv", "w", newline="", encoding='utf-8') as f:
    csvw = csv.writer(f)
    for v in noun_list:
        csvw.writerow(v)
