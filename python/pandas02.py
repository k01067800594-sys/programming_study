import pandas as pd





num=[1,2,3,4,5]
score_java=pd.Series([98,76,60,85,80], index=num)
score_python=pd.Series([88,92,100,55,70], index=num)

print(score_java)
print(score_python)

# java, python 시리즈 합계
total=score_java+score_python
print("덧셈 결과는")
print(total)
# index끼리 각각 연산

print("index 기준 내림차순 정렬")
print(total.sort_index(ascending=False)) 
print("값 기준 오름차순 정렬")
print(total.sort_values(ascending=True)) # 기본값으로 생략
print("값 기준 내림차순 정렬")
print(total.sort_values(ascending=False))