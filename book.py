class Book():
    def __init__(self,title,author,isbn,bibliography, quantity=1) :
        self.title : str = title
        self.author : str = author
        self.isbn = isbn
        self.bibliography = bibliography

        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.bibliography}"
    
    def borrow(self) :
        if self.quantity > 0 :
            self.quantity-=1
            return self
        else :
            return None
        
    def info(self) :
        print("Here is some info on this book: ")
        print(f"Name: {self.title}\nAuthor: {self.author}\nBibliography: {self.bibliography}")

    def return_book(self) :
        self.quantity+=1
    
if __name__ == "__main__" :
    # print("this is hidden gang")
    book = Book("hunger games","jenifer lawrence",12563634,"murder")
    print(book)