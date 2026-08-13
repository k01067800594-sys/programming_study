# 1.점수리스트 선언
scores=[65,80,95,70,88,55]
# 2.len()을 사용하여 전체 학생 수 구하기
students=len(scores)
# 3.max()를 사용하여 최고점수 구하기
max_scores=max(scores)
# 4.min()을 사용하여 최저점수 구하기
min_scores=min(scores)
# 5,6.sum()과 len()을 사용하여 평균을 구하고, round()로 소수 첫째 자리까지 반올림
avg_scores=round(sum(scores)/students,1)
# 카운트용 변수 초기화
avg_count=0
pass_students=0
# 7,8. 반복문과 조건문을 사용하여 평균 이상 학생 수 및 합격자 수 계산
for score in scores:
    # 7.평균 점수 이상인지
    if score >=avg_scores:
        avg_count+=1
    # 8.70점 이상(합격)인지 검사
    if score>=70:
        pass_students+=1
# 9.sorted() 및 reverse=True를 사용하여 원본을 변경하지 않고 내림차순(높은 점수 순) 정렬
sorted_scores=sorted(scores, reverse=True)
print(f"전체 학생 수:{students}")
print(f"최고 점수:{max_scores}")
print(f"최저 점수:{min_scores}")
print(f"평균:{avg_scores}")
print(f"평균 이상 학생 수:{avg_count}")
print(f"합격자 수:{pass_students}")
print(f"내림차순:{sorted_scores}")