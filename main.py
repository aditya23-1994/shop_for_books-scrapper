from apps import books

def print_best_books():
    global books
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for books in best_books:
        return books

def print_cheapest_books():
    cheap_books = sorted(books, key=lambda x: x.price)[:10]
    for books in cheap_books:
        return books

def print_cheap_best_books():
    s1 = print_best_books()
    s2 = print_cheapest_books()

    books = s1.intersection(s2)

    return books
