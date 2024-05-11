class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListSearch(head,data):
    iterator = head
    i = 0
    while iterator is not None:
        if iterator.data == data:
            return i
        i += 1
        iterator = iterator.next
    return -1
