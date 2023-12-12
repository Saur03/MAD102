#Create the book class
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

#introduction

bookshelf = []
addBook = ''

while addBook != 'Q':
    #get the user to enter a title - then the author
    title = input('Please enter a book title: ').title()
    author = input('Please enter the author\'s name: ').title()

    #create an book instance
    book = Book(author, title)

    #add the book to the list
    bookshelf.append(book)

    addBook = input('Hit Enter to add more books or Q to quit: ').upper()

print('Here are the books')

for book in bookshelf:
    print(f'{book.title} is written by {book.author}')

print('All done')


