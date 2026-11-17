class Book:
    def __init__(self,title,author):
        self.title= title
        self.author= author
        self.is_available= True
    def display_info(self):
        print("Book name: "+ self.title)
        print("author: "+ self.author)
        print("Available: "+ str(self.is_available))

       