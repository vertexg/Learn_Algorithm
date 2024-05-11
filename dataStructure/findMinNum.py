class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMinNum(head):
        min = head.data
        cur = head
        id = 0
        while cur is not None:
            if(cur.data <= min):
                min = cur.data
                min_id = id
            id += 1
            cur = cur.next
            
        return min_id 
