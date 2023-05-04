'''class library():
    def __init__(self,no_of_books,books):
        self.n=no_of_books
        self.books=books
    def display(self):
        for i in self.books:
            print(f"The books u entered are{i}")
    def check(self):
        c=0
        for i in self.books:
            c+=1
        if(c!=self.no_of_books):
            print(\'''Error!!
Your books is not Equal to no. of books\''')'''
class library():
    def __init__(self):
        self.n=0
        self.books=[]
    def add(self,book):
        self.books.append(book)
        self.n=len(self.books)
    
    def display(self):
        for i in self.books:
            print(f"The books u entered are:-{i}")
        
            
        
        
            
        
