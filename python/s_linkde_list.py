# 단일 연결 리스트 : 노드가 data와 link로 구성

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
print("저장 값:", node1.data)
print("다음 노드:", node1.next)

# 노드 세개 연결하여 출력
class Node2:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node2(10)
head.next=Node2(20)
head.next.next=Node2(30)

cur=head

while cur is not None: # None이 아닐때까지 반복
    print(cur.data) # 노드의 값을 출력
    cur=cur.next # 다음노드로 현재위치를 변경

# -------------------------------------------
class Node3:
    def __init__(self, data):
        self.data=data
        self.next=None

class S_list:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node3(data) # 새노드 등장

        if self.head is None: # 노드가 전혀 없으면
            self.head=new_node # 새로운 노드부터 시작
            return
        
        curr=self.head # 첫 위치를 현재위치로도 정함

        while curr.next is not None: # 끝까지 이동(None 일때까지)
            curr=curr.next # 뒤로 하나씩 이동

        curr.next=new_node # 마지막 노드 위에 새 노드 연결

    def print_list(self):
        curr=self.head
        if curr is None:
            print("연결리스트가 비어있습니다")
            return
        while curr is not None:
            print(curr.data, end="->")
            curr=curr.next
        print("None")

        # 맨앞에 새노드 삽입
    def insert_first(self, data):
        new_node=Node3(data) # 새노드 생성

        new_node.next=self.head
        # 처음위치를 새노드의 다음위치 변경
        self.head=new_node
        # 새노드를 가장 앞으로 삽입
    def length(self):
        count=0
        curr=self.head

        while curr is not None:
            count+=1
            curr=curr.next

        return count
    # 노드 삭제
    def delete(self, target):
        if self.head is None:
            print("삭제할 노드가 없음")
            return
        # 첫번째 노드가 삭제 대상인 경우
        if self.head.data==target:
            self.head=self.head.next
            print(target,"삭제 완료")
            return
        curr =self.head
        while curr.next is not None:
         if curr.next.data==target:
             curr.next=curr.next.next
             print(target,"삭제완료")
             return
         curr=curr.next
    print("값을 찾지 못함")

s=S_list()
s.append(100)
s.append(200)
s.append(300)
s.insert_first(5)
s.length()
print("노드 갯수",s.length())
s.delete(200)
s.delete(550)
s.print_list()
