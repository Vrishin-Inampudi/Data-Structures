class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return False
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp is None:
                    temp.left = new_node
                    return True
                temp = temp.left 

            else:
                if temp.right == None:
                    temp.right == new_node
                    return True 
                temp = temp.right
    
    def contains_value(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True 
        return False
    
    def __r_contains(self,current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left,value)
        if value > current_node.value:
            return self.__r_contains(current_node.right,value)

    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def __r_insert(self,current_node,value):

        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node




    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)


                    

            
            
