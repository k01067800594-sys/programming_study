print("*args로 여러개의 값 받기")

class Calc:
    def add(self, *nums):
        tot =0
        for i in nums: 
           #튜플에서 하나씩 꺼내서 끝까지 반복
           tot += i
        return tot

c = Calc()
print(c.add(10,20))
print(c.add(10,20,30))
print(c.add(10,20,30,40,50))

# =============================
#isinstance(값, 자료형)
# 결과가 Ture/False

class Type_class:
    def t_data(self, data):
        if isinstance(data, int):
            print("정수입니다.")
        elif isinstance(data, str):
            print("문자열입니다.")
        elif isinstance(data, list):
            print("리스트입니다.")
        else:
            print("없는 자료형입니다.")

t = Type_class()
t.t_data(100)
t.t_data("파이썬")
t.t_data([10,20,30])
t.t_data(54.25)