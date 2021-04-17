
# create a class library
# display book
# lend book
# add book
# return book
# harrylibrary=library(libararybooks,libararyname)

class library:
    books=["Harry Potter","love","Feel for you","Start building your self up"]

    def displaybooks(self):
        return F"Your list of books is:{self.books}"
    def addbooks(self):
        return  self.books.append(input("What is your book name you want to add:"))

    def withdrawnooks(self):
        print(input("What is your name:"))
        a=input("What is Your book name you want to take:")
        if  a=="Harry Potter" or a=="love" or a=="Feel for you" or a=="Start building your self up":
            return self.books.pop(input("You have taken the book"))
        else:
            return "you have given wrong input"

    def returnbooks(self):
        return  self.books.append(input("What is your book name you want to add:"))

ankit=library()

import time
i=1
while(i!=10):
    print("Your Option's' are:\n"" Display Books:D\n","Add Books:A\n","Withdraw Books:W\n","Return Books:R")
    i = i + 1
    x = input("Put Your choice here:")

    D="Display Books"
    A="addbooks"
    W="withdraw books"
    R="return books"
    if x=='D':
        print(ankit.displaybooks())
    elif x=='A':
        print(ankit.addbooks())

    elif x=='W':
        print(ankit.withdrawnooks())

    elif x=='R':
        print(ankit.return1books())
    time.sleep(5)



