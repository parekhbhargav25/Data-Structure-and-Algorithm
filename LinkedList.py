class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__ (self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList (self):
        temp = self.head
        while(temp is not None ):
            print(temp.value)
            temp = temp.next
    

    def append (self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = None
            self.tail = None
        else:
            self.tail.next= new_node
            self.tail = new_node
        self.length += 1
        return True
    
    
    def pop(self):
        pre = self.head
        temp = self.head

        if self.length == 0: 
            return None
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None

        self.length -= 1
        if (self.length  == 0):
            self.head = None
            self.tail =None
        return temp
    def prepend(self,value):
        new_node = Node (value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
             new_node.next = self.head
             self.head = new_node
        self.length += 1
        return True
    
    def PopFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head =  self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp
    def get (self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range (index):
            temp = temp.next
        return temp
    def set_value (self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    def insert(self, index,value ):
        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index -1) 
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    def remove (self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.PopFirst()
        if  index == self.length:
            return self.pop()
        # temp = self.get(index)
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
       temp = self.head
       self.head = self.tail
       self.tail = temp

       after = temp.next
       before = None

       for _ in range (self.length):
           after = temp.next
           temp.next = before
           before = temp
           temp = after







        
        




        

myLinked_list = LinkedList(1)
myLinked_list.append(2)
myLinked_list.append(3)
myLinked_list.append(4)
myLinked_list.append(5)

# myLinked_list.printList()

myLinked_list.set_value(2,10)
# myLinked_list.printList()

myLinked_list.insert(2,15)

myLinked_list.remove(3)
myLinked_list.printList()


        






# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next = None




# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
    
#     def print_list (self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

    # def append (self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next= new_node
    #         self.tail = new_node
    #     self.length += 1
    #     return True
#     def pop(self):
#         pre = self.head
#         temp = self.head
#         if self.length ==0:
#             return None
        
#         # For two or more nodes
#         while(temp.next is not None):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1

#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp


# myLinked_list = LinkedList(1)
# myLinked_list.append(2)

# myLinked_list.print_list()

# print(myLinked_list.pop())
# print(myLinked_list.pop())
# print(myLinked_list.pop())





















































# # class Node:
# #     def __init__ (self,value):
# #         self.value = value
# #         self.next = None

# # class LinkedList:
# #     def __init__(self,value):
# #         new_node = Node(value)
# #         self.head = new_node
# #         self.tail = new_node
# #         self.length = 1


# # my_linked_lst = LinkedList(4)

# # print(my_linked_lst.head.value)