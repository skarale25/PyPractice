class Book:
    def __init__(self, title, author, edition, cost):
        self.title = title
        self.Author = author
        self.Edition = edition
        self.cost = cost
        print("Title: ", self.title)
        print("Author: ", self.Author)
        print("Edition: ", self.Edition)
        print("Cost: ", self.cost)


b = Book('Learning Python', 'Mavle Lutz', 5, 100)
