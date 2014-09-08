#-*- coding:utf-8 -*-

class Book:
    books=[]
    def __init__(self,bid,details=None):
        self.bid=bid
        self.details=details

    @classmethod
    def delete(cls,book):
        cls.books.remove(book)

    @classmethod
    def add(cls,book):
        cls.books.append(book)

    @classmethod
    def find(cls,bid):
        for b in cls.books:
            if bid==b.bid:
                return b

b1=Book(1)
b2=Book(2)
Book.add(b1)
Book.add(b2)
print(Book.find(1).bid)
Book.delete(b2)
for i in Book.books:
    print(i.bid)


