search_book = input()
num_book = int(input())
count = 0
book = input()
while num_book:
    if search_book == book:
        print(f"You checked {count} books and found it.")
        break
    else:
        count += 1
        if count == num_book:
            print(f"The book you search is not here!")
            print(f"You checked {count} books.")
            break
    book = input()
