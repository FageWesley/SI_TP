import json
import socketserver

#region Book
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
            return {
                'name': obj.name,
                'tag': obj.tag,
                'image': obj.image
                }
        return super().default(obj)
#endregion
#region Library 
class Library:
    library = None

    @classmethod
    def get_instance(cls):
        if cls.library is None:
            cls.library = Library()
        return cls.library

    def __init__(self):
        self.__books = []

    
    def add_book(self,book):
        self.__books.append(book)

    def display_books(self):
        books = ''
        for book in self.__books:
            books += f'{book}\n' 
        return books

    def remove_book(self,name):
        book_to_delete = None
        for book in self.__books:
            if book.name == name:
                book_to_delete = book
        self.__books.remove(book_to_delete)

    def save(self):
        with open('library.json','a') as output:
            output.write(json.dumps(self.__books, cls=BookEncoder))
#endregion
#region Server
class Server(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode('utf-8')
        print("Received from {}:".format(self.client_address[0]))
        response = ''
        if self.data == 'list':
            response = f'List: {Library.get_instance().display_books()}'
        # just send back the same data, but upper-cased
        if self.data.startswith('add'):
            command,name,tag,image = self.data.split(',')
            book = Book(name,tag,image)
            Library.get_instance().add_book(book)
            response = f'Adding {book} to library'

        self.request.sendall(bytes(response, "utf-8"))

#list : list books
#add : add book
#remove : remove book

    
#endregion
        

if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), Server) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

    lib = Library()
    book = Book('Python','Programming','python.jpg')
    lib.add_book(book)
    lib.display_books()

    pass