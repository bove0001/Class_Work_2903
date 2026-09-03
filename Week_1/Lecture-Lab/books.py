class Author:
    def __init__(self, name):
        self.name = name       # the author's name
        self.books = []        # thier books list starts empty

    def publish(self, title):
        # add the new book title to the author's list of books
        self.books.append(title)

    def __str__(self):
        # seperate the book titles with commas for a clean output
        if not self.books:
            # handle the case where no books have been published yet
            return f'{self.name} has not published any books yet'
        book_list = ', '.join(self.books)
        return f'{self.name} has published: {book_list}'


def main():
    # create a couple example authors
    author1 = Author('J.K. Rolling')
    author2 = Author('George Orwell')
    author3 = Author('Clara Jones')

    # publish some example books
    author1.publish("Harry Potter and the Sorcerer's Stone")
    author1.publish('Harry Potter and the Chamber of Secrets')
    author2.publish('1984')
    author2.publish('Animal Farm')

    # print the authors and thier books
    print(author1)
    print(author2)
    print(author3)


main()