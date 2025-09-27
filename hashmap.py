class HashTable:
    def __init__(self,size = 8):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0 #default value
        for letter in key: #iterates for every letter of the key
            my_hash = (my_hash+ord(letter)*23 %len(self.data_map)) 
        return my_hash 
    '''
    my_hash = (my_hash+ord(letter)*23 %len(self.data_map)) 
    ord converts the letter to ascii * by a prime number to reduce collisions 
    and the modulo of the len(self.data_map) gives you a bounds within the bucket size
    this itterates throught the entire word or string 
    '''
    
    def set_item(self,key,value):
        index = self.__hash(key) #uses __hash for the index
        if self.data_map[index] is None: #if there is nothing at the index 
            self.data_map[index] = [] #make a new list and the index 
        self.data_map[index].append([key,value]) #line that adds the code to the list 

    def get_item(self,key):
        index = self.__hash(key) #find the index of the key we're trying to get
        if self.data_map[index] is not None: #if the index isn't none (meaning it does actually exist)
            for pair in self.data_map[index]: #iterate through every pair int he index we get 
                if pair[0] == key: # if the pair at value 0 equals key value we're looking for
                    return pair[1] # return the pair    
        return None # if nothing is returned return none
    
    

        



