class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListLastValue(head):
    iterator = head

 
    if iterator is None:
        return None

    while iterator.next is not None:
        iterator = iterator.next

    return iterator.data
