#create a class book
#attributes - name,author,pages,type(fiction,non fiction)
#constructor

#is_fiction()--> True if book belongs to fiction category otherwise false
#is_nonfiction()--> True if book belongs to nonfiction category otherwise false
#time_to_read()--> returns 5 days if number of pages <100
#returns 20 days if number of pages between 100 and 500(including 500)
#return infinite if number of pages >500
#same_author(self,book) which returns true if two books have the same author.book is of type Book

class Book:
    def __init__(self,name,author,page,category):
        self.name = name
        self.author = author
        self.page = page
        self.category = category

    def is_fiction(self):
        if self.category == "fiction":
            return True
        return False

    def is_nonfiction(self):
        if self.category == "nonfiction":
            return True
        return False
    
    def time_to_read(self):
        if self.page <=100:
            return "5 days"
        elif self.page > 100 and self.page <=500:
            return "20 days"
        else:
            return "infinity"

    def same_author(self,book):
        if self.author == book.author:
            return True
        return False


book1_details = input("enter the name,author,page,category of book seperated by comma").split(",")
book1_details[2] = int(book1_details[2])
book2_details = input("enter the name,author,page,category of book seperated by comma").split(",")
book2_details[2] = int(book2_details[2])

book1=Book(*book1_details)
book2=Book(*book2_details)

print(book1.is_fiction(),book1.is_nonfiction(),book1.time_to_read())
print(book2.is_fiction(),book2.is_nonfiction(),book2.time_to_read())

print(book1.same_author(book2))
