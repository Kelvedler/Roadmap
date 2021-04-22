class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title: {}; Author: {}; Pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book {} is destroyed'.format(self.title))


b = Book('Python', 'Jose', 200)
print(b)
print(len(b))
del b

