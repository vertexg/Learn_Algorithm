class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListLength(head):
    c = 0
    currentNode = head
    while currentNode is not None:
        c  += 1
        currentNode =currentNode.next
    return c
