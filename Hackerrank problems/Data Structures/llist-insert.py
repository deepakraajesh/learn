class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))
        node = node.next
        if node:
            print(sep)

def insertNodeAtPosition(llist, data, position):
    newNode = SinglyLinkedListNode(data)
    currNode = llist
    index = 0
    print(type(currNode))
    while index < position-1:
        currNode = currNode.next
        index+=1
    nextNode = currNode.next
    currNode.next = newNode
    newNode.next = nextNode
    return llist

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, ' ')