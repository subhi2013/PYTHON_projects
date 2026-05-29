books = {}
def add_book():
    book_name =input("enter book name:")
    books[book_name] = "available"
    print("book added")
def show_books():
    if len(books) == 0:
        print("no books found")
    else:
        for book in books:
            print(book , ":" , books[book])
def search_book():
    book_name = input("enter book name:")
    if book_name in books:
        print("status:" , books[book_name])
    else:
        print("book not found")
def issue_book():
    book_name = input("enter book name:")
    if book_name in books:
        books[book_name] = "issued"
        print("book issued")
    else:
        print("book not found")
def return_book():
    book_name = input("enter book name:")
    if book_name in books:
        books[book_name] = "availabale"
        print("book returned")
    else:
        print("book not found")
def delete_book():
    book_name = input("enter book name:")
    if book_name in books:
        del books[book_name]
        print("book deleted")
    else:
        print("book not found")
def count_books():
    print("total books:" , len(books))
def count_available_books():
    total = 0
    for book in books:
        if books[book] == "available":
            total = total + 1
        print("available books" , total)
def count_issued_books():
    total = 0
    for book in books:
        if books[book] == "issued":
            total = total + 1
        print("issued books:" , total)
def save_books():
    with open("books.txt" , "w" , encoding = "utf-8") as file:
        for book in books:
            file.write(book + "," + books[book] + "\n")
    print("books saved")
def load_books():
    try:
        file = open("books.txt" , "r" , encoding="utf-8")
        for line in file:
            line = line.strip()
            book , status = line.split(",")
            books[book] = status
        file.close()
        print("books loaded")
    except FileNotFoundError:
        print("file not found")
while True:
    print("\n-------library management system-------\n")
    print("1. add books")
    print("2. show books")
    print("3. search books")
    print("4. issue books")
    print("5. return books")
    print("6. delete books")
    print("7. count books")
    print("8. count available books")
    print("9. count issued books")
    print("10. save books")
    print("11. load books")
    print("12. exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        add_book()
    elif choice == 2:
        show_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        delete_book()
    elif choice == 7:
        count_books()
    elif choice == 8:
        count_available_books()
    elif choice == 9:
        count_issued_books()
    elif choice == 10:
        save_books()
    elif choice == 11:
        load_books()
    elif choice == 12:
        print("program ended")
        break
    else:
        print("choice not found")
        
    