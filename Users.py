class User:
    def __init__(self,name,id_user):
        self.name=name
        self.id_user=id_user
class librarian(User):
    def __init__(self,name,id_user):
        super().__init__(name,id_user)
        self.Book_list=[]
    def add_Book(self,Book_title):
        self.Book_list.append(Book_title)
        print("librarian added the book: "+ Book_title)