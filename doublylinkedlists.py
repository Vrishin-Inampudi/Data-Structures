class Node: #make a new node 
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value): #If nothing exists 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def print_list(self): #print 
        temp = self.head
        while self.head is not None:
            print(temp.value)
            temp = temp.next


    def appened(self,value): #add to the end of the list
        new_node = Node(value) #make new node
        if self.head is None: #if nothing in linked list
           self.head,self.tail = new_node #use the head and tail to point to the new_node
        else: #if there are value 
            self.tail.next = new_node #the tails next value points to the new node
            new_node.prev = self.tail #now the tail points to the new_node
        self.length += 1 # increase the length by one 
        return True #need it for something else
    
    def pop(self,value): #pull last value
        if self.length == 0: #nothing in list 
            return None #return nothing
        temp = self.tail #need a variable to hold the value  
        if self.length == 1: #if we have one thing in the list 
            self.head = None #change the head to none 
            self.tail = None #tail to none
        else: #No other conditions    
            self.tail = self.tail.prev #change the tail to the previous value
            self.tail.next = None #change the next value to none
            temp.prev = None #change the temps prev pointer to none
        self.length -= 1 #decrement the list by one 
        return temp #return the value 
    
    def prepend(self,value):
        new_node = self.value #make a new node 
        if self.length == 0: # if nothing in the list
            self.head,self.tail = new_node #make the list with the value 
        else: #else
            new_node.next = self.head #change the head to be the next value in new_node
            self.head.prev = new_node #the self.head previous value is now the new node
            self.head = new_node #change the head to the new_node
        self.length += 1 #increase the length by one 

    def pop_first(self):
        
        if self.length == 0: #if nothing in the list 
            return None #return nothing
        temp = self.head #need something to clone the first value
        if self.length == 1: #if we have one thing in the list 
            self.head == None #head is now none 
            self.tail == None #tail is now none
        else:
            self.head = self.head.next #move head up
            self.head.prev = None #break of connection
            temp.next = None #temp next value shouldn't be pointing at anything 
        self.length -= 1 #decrease the length 
        return temp #return the value 
    
    def get(self,index):
        if index < 0 or index >= self.length: #if the index is not in the scope of the list 
            return None #nothing to get
        temp = self.head # set the head = temp
        if index < self.length/2: #if the index is on the left half use the head to start iterating
            for _ in range(index): #iteration index is the the number of times iterating 
                temp = temp.next #next value
        else:
            temp = self.tail #use the tail to start iterating 
            for _ in range(self.length -1, index, -1): #iterate downwards 
                temp = temp.prev #climb through the list
        return temp #return the value 
        
    def set_value(self,index,value): #set a value at an index
        temp = self.get(index) #set temp to value at index
        if temp: #if temp exists 
            temp.value = value #change temp.value to the value we want 
            return True #return true 
        return False #else basically return false
    
    def insert(self,value,index): 
        if index < 0 or index > self.length: #if index is out of scope 
            return False #return that it doesnt work 
        if index == 0: #if index is zero 
            self.prepend(value) #use the prepend value 
        if index == self.length-1: #if index is the length-1 
            self.appened(value) #use apppened the value 
       #after if statements 
        new_node = Node(value) 
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node 
        after.prev = new_node 

        self.length += 1
        return True 
    
    def remove(self,index):
        
        if index < 1 or index >= self.length:
            return None
        if index == 0:
            self.pop_first(index)
        if index == self.length -1:
            self.pop(index)

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev 

        self.length -= 1 
        return temp
        
   


        






        







