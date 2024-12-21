class book:
   def __init__(self, title, author):
      self.title = title
      self.author = author
    
book1 = book ("diary of a wimpy kid", "jef kinney")
book2 = book ("secret class", "wang kang cheol")
del book1.author
print(book2.title, book2.author)
print(book1.title, book1.author)
