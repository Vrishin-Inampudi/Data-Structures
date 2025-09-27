class ListMap:
    def __init__(self):
        self.items = [] #empty list 

    def get(self, key):
        for k, v in self.items: #for every key value pair in self.items
            if k == key: #if the key and k value are equal
                return v #return the value 
        raise KeyError(f"Key {key} not found") #if nothing is found raise error 

    def put(self, key, value):
        for i, (k, _) in enumerate(self.items): #for every value for how many keys you have in every index - enumerate.
            if k == key:
                self.items[i] = (key, value) #replace whatever you want at the current index 
                return #break the loop if completed 
        self.items.append((key, value)) #if nothing is there just add it yourself

    def remove(self, key):
        for i, (k, _) in enumerate(self.items): #for every value for how many keys you have in every index - enumerate.
            if k == key:
                self.items.pop(i) #pop the value 
                return
        raise KeyError(f"Key {key} not found")#can't be found 

    def contains(self, key):
        return any(k == key for k, _ in self.items)

    def __len__(self):
        return len(self.items)
