# 워드 클라우드(word cloud)
# - 특정 단어릐 빈도나 중요성을 글자의 크기로 나타낸 이미지

from collections import Counter
from kiwipiepy import Kiwi
import matplotlib.pyplot as plt
from wordcloud import WordCloud

kiwi = Kiwi()

text ="""
이듬해 질 녘 꽃 피는 봄 한여름 밤의 꿈
가을 타 겨울 내릴 눈 1년 네 번 또다시 봄

정들었던 내 젊은 날 이제는 안녕
아름답던 우리의 봄 여름 가을 겨울

“Four season with no reason.”
비 갠 뒤에 비애(悲哀) 대신 a happy end
비스듬히 씩 비웃듯 칠색 무늬의 무지개
철없이 철 지나 철들지 못해(still)
철부지에 철 그른지 오래 Marchin’ 비발디
차이코프스키 오늘의 사계를 맞이해
마침내 마치 넷이 못내

Boy 저 하늘만 바라보고서
사계절 잘 지내고 있어 Good-bye
떠난 사람 또 나타난 사람
머리 위 저세상
난 떠나 영감의 amazon
지난 밤의 트라우마 다 묻고
목숨 바쳐 달려올 새 출발 하는 왕복선
변할래 전보다는 더욱더
좋은 사람 더욱더
더 나은 사람 더욱더
아침 이슬을 맞고 내 안에 분노 과거에 묻고
For Life

울었던 웃었던 소년과 소녀가 그리워 나
찬란했던 사랑했던 그 시절만 자꾸 기억나

계절은 날이 갈수록 속절없이 흘러
붉게 물들이고 파랗게 멍들어 가슴을 훑고

언젠가 다시 올 그날 그때를 위하여 (그대를 위하여)
아름다울 우리의 봄 여름 가을 겨울

La la la la la la la la la la la
La la la la la la la la la la la
La la la la la la la la la la la
La la la la la la la la la la la

이듬해 질 녘 꽃 피는 봄 한여름 밤의 꿈
가을 타 겨울 내린 눈 봄 여름 가을 겨울
"""

# 2. 형태소 분석 진행
tokens=kiwi.tokenize(text)
word_list = []

# 3. 명사(NNG, NNP)와 형용사(VA) 추출
for token in tokens:
    if token.tag in ['NNG', 'NNP', 'VA']:
        # token.form : 단어 본래의 형태
        word_list.append(token.form)

# 3. 단어 빈도수 계산
word_list_count = Counter(word_list)

# 4. 워드클라우드 객체 생성
wc = WordCloud(
    font_path='malgun',
    width=400,
    height=400,
    background_color='white', # 배경색을 흰색으로 변경
    )

# 5. 빈도수 데이터로 워드클라우드 생성
result=wc.generate_from_frequencies(word_list_count)

# 6. matplotlib로 출력
plt.figure(figsize=(6, 6)) # 출력 이미지 크기 설정
plt.imshow(result, interpolation='bilinear')
plt.axis('off') # 축 레이블 제거
plt.show() 