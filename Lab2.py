#LinkedListPractice
class Node(object):
    def __init__(self,data = None,count = 0,next = None):
        self.data = data
        self.count = count
        self.next = next
        
    def getData():
        return self.data
        
class LinkedList:
    def __init__(self,head = None):
        self.head = head

    def addFirst(self, data):
#        temp = Node(data,self.head)
        self.head = Node(data,1,self.head)

    def printList(self):
            print("LIST")
            temp = self.head
#           print(self.head.data)
            while temp is not None:
                print(temp.data)
                print("count:", temp.count)
                temp = temp.next 
                
    def find(self,x):
        if self.head is None:
            return False
        curr = self.head
        while curr is not None:
            if curr.data == x:
                curr.count +=1
                return True
            else:
                curr = curr.next
        return False
            
    def length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next 
            
        return count
    #Merge does Not WORK
    #####3
#    def mergeSort(self):
#        temp = self.head
#        if temp is None or temp.next is None:
#            return
#        left, right = splt(self)
#        left = mergeSort(left)
#        right = mergeSort(right)
#        return combine(left,right)
#        
#    def splt(self):
#        temp = self.head
#        if temp is None or temp.next is None:
#            left = temp
#            right = None
#            return left, right
#        else:
#            mid = temp
#            t = temp.next
#            while t is not None:
#                t = t.next
#                if t is not None:
#                    t = t.next
#                    mid = mid.next
#        left = temp
#        right = temp.next
#        mid.next = None
#        return left, right
#    
#    def combine(left,right):
#        result = Node("", -1, None)
#        curr = result
#        while left and right:
#            if left.count > right.count:
#                curr.next = left
#                left.left.next
#            else:
#                curr.next = right
#        if left is None:
#            curr.next = right
#        if right is None:
#            curr.next = left
#        return result.next
#        
    def bubble(self):
        finish = None
        while finish != self.head:
            start = self.head
            while start.next != finish:
                index = start.next
                if start.count < index.count:
                    start.data, index.data = index.data, start.data
                    start.count, index.count = index.count, start.count
                start = start.next
            finish = start

ll = LinkedList()

file = open("10-million-combos.txt", "r")
    #read each line at a time
read = file.readlines()

for line in read:
    #splits each element into list
    array = line.split("	")
    if (ll.find(array[-1]) == False):
        ll.addFirst(array[-1])
        

ll.printList()
ll.bubble()
ll.printList()

#SOLUTION B
dict = {}
file = open("testcase1.txt", "r")
read = file.readlines()
for line in read:
    array = line.split("	")
    if array[-1] in dict:
        dict[array[-1]] = dict[array[-1]] + 1
    else:
        dict[array[-1]] = 1
        
for i in dict:
    print(dict[i])