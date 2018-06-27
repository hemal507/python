class buk():
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def display(self):
         print "P book: " + self.name + " : P Author is :  " + self.author


class cbuk(buk):
    def __init__(self,name,author,cost):
         buk.__init__(self,name,author)
         self.cost=cost
    def display2(self):
        print "C book: " + self.name + " : C Author :" + self.author + " C. cost : " , self.cost
                         
a=cbuk('z','m',20)
a.display2()
a.display()

