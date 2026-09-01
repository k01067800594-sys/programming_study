import pandas as pd
# 2차원 구조(DataFrame)

score=pd.DataFrame(
    [
    [100,30,40,55,77],
    [100,30,40,55,77], # Java
    [50,66,100,78,90], # Python
    [20,78,99,80,70] # C
    ],
    index=["Java","Python","C"]
)
print(score)
print("\n")

num=[1,2,3,4,5]
score2=pd.DataFrame(
    {
    "name":["홍길동", "이길동", "장길동", "오길동", "최길동"],
    "java":[100,30,40,55,77],
    "python":[50,66,100,78,90],
    "C":[20,78,99,80,70]
    },
    index=num
)
print(score2)
print(score2.head(2))
print(score2.tail(2))
print("index 기준 내림차순 정렬")
print(score2.sort_index(ascending=False))
print(score2.sort_values(by="name", ascending=True))

score3=score2.sort_values(by="java", ascending=False)
print(score3)

score3.to_csv("./score.csv", encoding="utf-8-sig")
