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
    def inserAt(self,position,value):
        self.position = position
        self.value = value
        node = LinklistNode(value)
        curr = self.head
        while curr.value != position:
            curr = curr.nextNode
        node.nextNode = curr.nextNode
        curr.nextNode = node

    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            temp = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = temp
        self.head = prev
    def delete(self,value):
        curr = self.head
        while curr.value != value:
            prev = curr
            curr = curr.nextNode
        prev.nextNode = curr.nextNode
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
linklist.inserAt(10,90)
linklist.delete(37)
linklist.printList()