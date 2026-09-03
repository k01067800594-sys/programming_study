from collections import Counter
from kiwipiepy import Kiwi

#pip install kiwipiepy
# 1. kiwi 객체 생성
kiwi = Kiwi()

text ="""
인공지능과 데이터 분석 시대에 파이썬의 중요성은 매우 큽니다.
파이썬은 데이터 분석과 인공지능 개발에 가장 적합하고 유용합니다.
파이썬을 활용하면 빅데이터 분석을 쉽게 할 수 있으며, 시각화 라이브러리도 매우 다양합니다.
따라서 데이터 분석가와 개발자에게 파이썬 학습은 정말 필요합니다.pi
"""

# 2. 형태소 분석 진행
tokens=kiwi.tokenize(text)
word_list = []

# 3. 명사(NNG, NNP)와 형용사(VA) 추출
for token in tokens:
    if token.tag in ['NNG', 'NNP', 'VA']:
        # token.form : 단어 본래의 형태
        word_list.append(token.form)

print("추출된 단어 리스트:")
print(word_list)

print("\n단어 빈도수:")
print(Counter(word_list))
