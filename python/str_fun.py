class SimpleBook:
    def __init__(self, title, price):
        self.title=title
        self.price=price
    def __str__(self):
        return f"도서명: {self.title}, 가격: {self.price}원"

s=SimpleBook("파이썬기초",20000)
print(s)
# s라는 객체를 출력하려고 하면 자동으로 __str__ 메서드를 호출
# __str__ 메서드 : 원하는 포멧으로 출력을 원할때 사용