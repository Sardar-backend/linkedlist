class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class queue:
    def __init__(self):
        self.front = self.rear =None
    def is_Empty(self):
        return self.front==None
    def Enqueue(self,data):
        new_ndoe=Node(data)

        if self.front== None:
            self.front = self.rear=new_ndoe
            return
        self.rear.next= new_ndoe
        self.rear = new_ndoe
    def Dequeue(self):
        if self.is_Empty():
            print("empty")
            return
        tmp= self.front
        self.front = tmp.next

        if self.front ==None:
            self.rear = None
q=queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
#print(str(q.front.data),str(q.rear.data))
#from queue import Queue

##q= Queue(maxsize=2)
##q.put(1)
##q.put(2)
##q.put_nowait(100)
##print(q.full())# اگر صف پر شده باشه ترو و گرنه فالس نشون ميده 
##print(q.get())# چنانچه خالي باشه هيچي بر نميگردونه فرانت يا اول داده بر ميگردونه
##print(q.empty())#اگه صف خالي باشه ترو وگرنه فالس نشون ميده
##print(q.get_nowait())# مثل گت با اين تفاوت که چنانچه صف خالي باشه ارور ميده
from collections import deque

q=deque()
q.append(10)
q.append(11)
q.append(12)
q.pop()#فرانت پاک ميکنه
q.popleft()#رير پاک ميکنه
print(q)
