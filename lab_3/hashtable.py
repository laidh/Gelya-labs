class HashTable:
    def __init__(self,size):
        self.table = {}
        self.size = size
    
    def insert (self, key, value):
        if len(self.table) < self.size:
            self.table[key] = value
        else:
            print("Table is full!")
    
    def delete(self,key):
        if key in self.table:
            del self.table[key]
    
    def search(self,key):
        return self.table.get(key, None)
    
    def printer(self):
        for key, value in self.table.items():
            print(f"{key}: {value}")
