
#31.10.2024 Wednesday
class Person:
    def __init__(self, name: str, age: int,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"I am {self.name}, {self.age} years old. {self.gender}."

class Member(Person):
    def __init__(self,name,age,gender,membership):
        Person.__init__(self, name, age, gender)
        self.membership = membership
    def introduce(self):
        return f"I am {self.name}, {self.age} years old. {self.gender}, with membership id {self.membership}."

class Author(Person):
    def __init__(self,name,age,gender,books_written):
        Person.__init__(self, name, age, gender)
        self.books_written = books_written
    def introduce(self):
        return f"Books written: {self.books_written}."

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership, books_written):
        Member.__init__(self, name, age, gender, membership)
        Author.__init__(self, name, age, gender, books_written)

    def introduce(self):
        return f"I am {self.name}, {self.age} years old. {self.gender}, with membership id {self.membership}. Books written: {self.books_written}"


members=[]
member1 = Member("jack",23, "male", 1234)
member2 = Member("lucy",43,"female",1233)
members.append(member1)
members.append(member2)
for member in members:
    print(member.introduce())

authors=[]
author1 = Author("Lucy",23,"female",["Brave","Hello"])
author2 = Author("David",30,"male",["Courage","Hi"])
authors.append(author1)
authors.append(author2)
for author in authors:
    print(author.introduce())

authormembers=[]
authormember1 = AuthorMember("Lucy",23,"male",1234,["Brave","Hello"])
authormember2 = AuthorMember("David",43,"male",1233,["Courage","Hi"])
authormembers.append(authormember1)
authormembers.append(authormember2)
for authormember in authormembers:
    print(authormember.introduce())


