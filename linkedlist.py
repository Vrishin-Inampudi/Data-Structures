class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node #head pointer
        self.tail = new_node #tail pointer 
        self.length = 1 #length of the list when initialized 

    def print_list(self):
        temp = self.head #sets the head value to temp
        while temp is not None: #while the pointer doesn't hit none
            print(temp.value) #print the value 
            temp = temp.next #move to next value and rerun the loop 

    def append(self,value):
        new_node = Node(value)
        if self.head is None: #if nothing in list 
            self.head = new_node #make a new list with the value you have 
            self.tail = new_node
            self.length = 1
        else: #if the list isn't empty 
            self.tail.next = new_node #tail pointer points to new node (appened adds to the end)
            self.tail = new_node #the tail pointer moves down to the new node 
        self.length += 1 #length increases because the value increases 
        return True #something for later 
    
    def pop(self,value):
        if self.length == 0:
            return None
        pre = self.head 
        temp = self.head 
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre #tail pointer is the previous value in the list 
        self.tail.next = None #tail pointer points to None
        self.length -= 1 
        if self.length == 0:
            self.head,self.tail = None
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None: #if nothing in list 
            self.head = new_node #make a new list with the value you have 
            self.tail = new_node
        else:
            new_node.next = self.head #new nodes next value is the previous head
            self.head = new_node #the new head is the new node 
        self.length += 1
        return True 
    
    def pop_first(self,value):
        if self.length == 0: #if the list has no values 
            return None #return none
        else:
            temp = self.head #setting the temp value to current head 
            self.head = self.head.next #changing the head to be the next value
            temp.next = None #disconnecting temp from LL by setting the next value to none 
            self.length -= 1 #list loses a value 
            if self.length == 0: #if the length is now 0 
                self.tail = None #make the head equal none
        return temp #pops the value

    def get(self,index):
        if index < 0 or index >= self.length: #if index is >= index or < 0
            return IndexError #no index 
        temp = self.head #need a pointer 
        for _ in range(index): #go through the LL till you reach the desired index
            temp = temp.next #next value after temp
        return temp #return the value when you reach the index
    
    def set_value(self,value,index):
        temp = self.get(index) #use the get function to find the index
        if temp is not None: #if temp isn't none (None is returned by chance)
            temp.value = value #change the value 
            return True #return true 
        return False #if previous conditions aren't met return false
    
    def insert(self,value,index):
        if index < 0 or index >= self.length: #if index is >= index or < 0
            return False #no index 
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value) #new node is made 
        temp = self.get(index - 1) #find the index right before 
        new_node.next = temp.next #
        self.value += 1
        return True 
    
    def remove(self,index):
        if index < 0 or index >= self.length: 
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop
        pre = self.get(index - 1)
        temp = pre.next 
        pre.next = temp.next
        temp.next = None
        self.length =- 1 
        return temp






    






      
          
       



            

    







