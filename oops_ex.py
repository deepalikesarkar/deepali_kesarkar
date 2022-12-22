class Books:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages
    def __add__(self, other):
        return(self.name+other.name,self.pages+other.pages)


obj1=Books('mrutunjay',450)
obj2=Books('yayati',500)
c=obj1+obj2
print(c)