#coroutines in python

def searcher():
    import time 
    book = "this is a book on lalu yadav and this book is good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is in the book")
        else:
            print("text is not in the book")


search = searcher
next(search)
search.send("yadav")