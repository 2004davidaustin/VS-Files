#0Name 1Chapters 2Book

max = ["", 0, ""]
print()

with open("w12books.txt") as books : 
    for book in books : 
        book = book.strip()
        book = book.split(":")
        book[1] = int(book[1])

        print(f"Scripture: {book[1]}, Book: {book[0]}, Chapters: {book[1]}")

        if book[1] > max[1] : max = book

print()
print(f"the book with most chapters is {max[0]} with {max[1]} chapters")
print()