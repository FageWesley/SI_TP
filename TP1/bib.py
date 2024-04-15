import json

class Book:
    def __init__(self,name,tag,image):
        self.__name = name
        self.__tag = tag
        self.__image = image
    
    @property
    def name(self):
        return self.__name
    
    @property
    def tag(self):
        return self.__tag
    
    @property
    def image(self):
        return self.__image
    

    def __repr__(self):
        return f'Book: {self.__name} ({self.__tag})'

class BookEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Book):
            return [obj.name, obj.tag,obj.image]
        return super().default(obj)
    
class Library:

    def __init__(self):
        self.__books = []

    
    def add_book(self,book):
        self.__books.append(book)

    def display_books(self):
        for book in self.__books:
            print(book)    

    def remove_book(self,name):
        book_to_delete = None
        for book in self.__books:
            if book.name == name:
                book_to_delete = book
        self.__books.remove(book_to_delete)

    def save(self):
        f = open('library.json','a')
        f.write(json.dumps(self.__books, cls=BookEncoder))

        
        

if __name__ == '__main__':
    lib = Library()
    book = Book('Python','Programming','python.jpg')
    lib.add_book(book)
    lib.display_books()
    lib.save()

    pass