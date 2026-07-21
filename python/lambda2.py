print("sort()와 람다함수")
# 리스트  안에 튜플
students =[
    ("홍길동", 60),
    ("권율", 92),
    ("이순신", 88),
    ("유관순", 74)
    ]
#sorted(정렬할 자료,key=정렬기준)
stu_list=sorted(students,key=lambda x : x[1])
print("오름차순")
print(stu_list)
for  a in stu_list:    
    print(a)

stu_list=sorted(students,
                key=lambda x : x[1],reverse=True)
# reverse : 역순(꺼꾸로)
print("내림차순")
print(stu_list)

print("=" * 50)
print("딕셔너리->리스트 의 정렬")
stu=[
    {"name":"홍길동","score":70},# item이 2개
    {"name":"아이유","score":88},
    {"name":"변우석","score":95},
    {"name":"유재석","score":52}
]  
# "name" ,"score" :키
#   "유재석", 52 : 값
#  점수 기준으로 내림차순
stu_desc = sorted(stu,
                key=lambda s : s["score"],
                reverse=True)

print("점수가 높은 순서부터 출력")

for ss in stu_desc:
    print(ss["name"],ss["score"])