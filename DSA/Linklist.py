class LinklistNode :
    def __init__(self,value , nextNode = None):
        self.value = value
        self.nextNode = nextNode
class Linklist :
    def __init__(self,head = None):
        self.head = head
    def insert(self,value):
        node = LinklistNode(value)
        if self.head == None:
            self.head = node
            return
        currNode = self.head
        while currNode.nextNode != None:
            currNode = currNode.nextNode
        currNode.nextNode = node
    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            temp = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = temp
        self.head = prev

    def printList(self):
        currNode = self.head
        while currNode != None:
            print(currNode.value,end=" -> ")
            currNode = currNode.nextNode
        print("None")
    
linklist = Linklist()
linklist.insert(1)
linklist.insert(3)
linklist.insert(4)
linklist.insert(6)
linklist.insert(10)
linklist.insert(37)
linklist.printList()
linklist.reverse()
linklist.printList()