class Publisher:
    def __init__(self,name):
        self.name=name
    def pubdisplay(self):
        print("Publisher = ",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def bookdisplay(self):
        self.pubdisplay()
        print("Title = ",self.title)
        print("Author = ",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,nopages):
        Book.__init__(self,name,title,author)
        self.price=price
        self.nopages=nopages
    def pythondisplay(self):
        self.bookdisplay()
        print("Price = ",self.price)
        print("No of pages = ",self.nopages)
p1=Python("computerbooks","Pythonprogramming","R K S",3000,350)
p1.pythondisplay()
