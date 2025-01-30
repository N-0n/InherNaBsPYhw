class polygon():
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    
class hexagon(polygon):
    def __init__(self, n1, n2):
        polygon.__init__(self,n1,n2)
        super().__init__(n1, n2)
        a=0.5*self.num1*self.num2*6
        print("Hexagon's area is ",a)

class decagon(polygon):
    def __init__(self, n1, n2):
        polygon.__init__(self,n1,n2)
        super().__init__(n1, n2)
        a=0.5*self.num1*self.num2*10
        print("Decagon's area is ",a)

class rectangle(polygon):
    def __init__(self, n1, n2):
        polygon.__init__(self,n1,n2)
        super().__init__(n1, n2)
        a=0.5*self.num1*self.num2
        print("Rectangle's area is ",a)

o1=hexagon(8,44)
o2=decagon(23,9)
o3=rectangle(71,2)

        
