# Node class
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        print("New node has been formed")
 
'''-------------------------------------------------------'''
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None

    '''--------------------------------------------'''

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)   # 1. Allocate the Node & Put in the data, & make next of new Node as head
        new_node.next = self.head   # 2. Move the head to point to new Node
        self.head = new_node
        print("The data",new_data,"has been inserted at the beginning ")

    '''--------------------------------------------'''

    # Inserts a new node after the given prev_node. This method is defined inside LinkedList class shown above
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:       # 1. check if the given prev_node exists
            print ("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)   # 2. Create new node & Put in the data
        new_node.next = prev_node.next # 3. Make next of new Node as next of prev_node
        prev_node.next = new_node   # 4. make next of prev_node as new_node
        print("The data",new_data,"has been inserted between the element ",prev_node)

    '''--------------------------------------------'''

    #Insert node in between
    def append(self, new_data):
        new_node = Node(new_data)      # 1. Create a new node and put in the data
        if self.head is None:          # 2. If the Linked List is empty, then make the new node as head
            self.head = new_node
            return
        last = self.head               # 3. Else traverse till the last node
        while (last.next):
            last = last.next
        last.next =  new_node          # 4. Change the next of last node
        print("The data",new_data,"has been appended at the end")

    '''--------------------------------------------'''

    #delete a node
    #Given a reference to the head of a list and a key, delete the first occurrence of key in linked list
    def deleteNode(self, key):  
        temp = self.head              # Store head node
        if (temp is not None):        # If head node itself holds the key to be deleted 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None):     # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None):           # if key was not present in linked list
            return
        prev.next = temp.next       # Unlink the node from linked list
        temp = None
        print("The given",key,"has been deleted from the linked list")

    '''--------------------------------------------'''

    #Delete the element at given position
    def deletePos(self, pos):
        if self.head is None:
            return
        if pos==0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == pos:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        print("The data at the given position",pos,"has been deleted")
        return prev

    '''--------------------------------------------'''
    #print linked list
    def printList(self):             # This function prints contents of linked list
        temp = self.head             # starting from head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    '''--------------------------------------------'''
    
    #Delete entire List
    def deleteList(self):
        current = self.head      # initialize the current node
        while current:
            prev = current.next  # move next node
            del current.data     # delete the current node
            current = prev       # set current equals prev node

        '''
        self.head = None         #In python garbage collection happens therefore, only self.head = None would also delete the link list
        '''
        print("The entire list has been deleted")

    '''--------------------------------------------'''

    # This function counts number of nodes in Linked List iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head          # Initialise temp
        count = 0                 # Initialise count
        while (temp):             # Loop while end of linked list is not reached
            count += 1
            temp = temp.next
        print ("Count of nodes is :",count)
        return count

    '''--------------------------------------------'''

    # Search for a value in linked list
    def search(self, x):
        current = self.head       # Initialize current to head
        count=0
        while current != None:    # loop till current not equal to None
            if current.data == x:
                print("Element is found at position: ",count)
                return True       # data found 
            current = current.next
            count+=1
        return False              # Data Not found

    '''--------------------------------------------'''

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head       # Initialise temp
        count = 0                 # Index of current node
        while (current):          # Loop while end of linked list is not reached
            if (count == index):
                print("Element at index",index,"is :",current.data)
                return current.data
            count += 1
            current = current.next
        assert(False)             # if we get to this line, the caller was asking for a non-existent element so we assert fail

    '''--------------------------------------------'''

    # Reverse the linked list
    def reverse(self):
        prev = None                  # Make a Null variable
        current = self.head          # Make 'current' as exisiting first head element
        while(current is not None):  # Recursively perform for each node
            next = current.next      # 1. Store the current next element in 'next'
            current.next = prev      # 2. Store the previous element in 'current.next'
            prev = current           # 3. Store the current element in 'prev'
            current = next           # 4. Store the next element in 'currrent'
        self.head = prev             # Make the prev element as 'head'
        print("The linked list has been reversed")
'''-------------------------------------------------------'''

# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()         # Start with the empty list
    '''
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
                                #Commenting this for learning purpose
    '''
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    #llist.head.next = second; # Link first node with second
    '''
    Now next of first Node refers to second.  So they
    both are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
    '''
    #second.next = third; # Link second node with the third node
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+
    '''
    llist.append('e')
    llist.push('a')
    llist.insertAfter(llist.head.next,'7')
    llist.append('f')
    llist.insertAfter(llist.head.next,'y')
    llist.deleteNode('y');    #Delete node with data 1
    llist.append('z')
    llist.push(1)
    llist.printList()
    print("\n")
    llist.deletePos(3)       #Delete node at position 3
    llist.printList()
    llist.getNth(3)
    llist.search('f')
    llist.reverse()
    llist.printList()
    llist.deleteList()