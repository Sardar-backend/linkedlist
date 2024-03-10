class Node:#کلاس براي ايجاد نود 
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:# کلاس براي ايجاد لينک ليست
    def __init__(self):
        self.head=None
    def inser_first(self,new_deta):# تابع برايجاد اولين نود 
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insert_last(self, new_data):#  تابع براي ايجاد اخرين نود 
        new_node=Node(new_deta)

        if self.head is None:
            self.head=new_node
            return
        tmp=self.head
        while(tmp.next):
            tmp=tmp.next
            tmp.next=new_node
    def inser_optional(self,prev_node,new_data):#  تابع براي ايجاد نود بين نود ها
        if prev_node is None:
            print("hey!! your node must be a node at the linkedlist")
            return
        new_node = Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def traverse(self):# 
        tmp = self.head
        while (tmp):
            print(tmp.data)
            tmp=tmp.next
my_linkedlist=linkedlist()
my_linkedlist.head=Node(1) # تابع براي داده دهي به نود اول
second_node = Node(2)# give data to second node
third_node = Node(3)# give data to third node
my_linkedlist.head.next=second_node # تنظيم نکست نود اول
second_node.next=third_node# تنظيم نکست نود دوم
my_linkedlist.inser_optional(second_node, 4)# تنظيم و داده دهي به نودي که ميان نود هاي ميخواهد باشد
my_linkedlist.traverse()# فراخواني براي سير در لينک ليست
