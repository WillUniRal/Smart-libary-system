class Book():
    def __init__(self,title,author,isbn,bibliography) :
        self.title = title
        self.author = author
        self.isbn = isbn
        self.bibliography = bibliography
    def __str__(self):
        return f"{self.title} by {self.author}\n{self.bibliography}"
    
if __name__ == "__main__" :
    # print("this is hidden gang")
    book = Book("hunger games","jenifer lawrence",12563634,"murder")
    print(book)