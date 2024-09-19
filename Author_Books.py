authorsbooks = {
    "J.K. Rowling": "Harry Potter",
    "George Orwell": "1984",
    "J.R.R. Tolkien": "The Lord of the Rings",
    "F. Scott Fitzgerald": "The Great Gatsby",
    "Harper Lee": "To Kill a Mockingbird",
    "Jane Austen": "Pride and Prejudice",
    "Mark Twain": "The Adventures of Tom Sawyer",
    "Ernest Hemingway": "The Old Man and the Sea"
}

entire_dict_authors = authorsbooks

fifth_author = list(authorsbooks.keys())[4]
fifth_author_book = authorsbooks[fifth_author]

seventh_author = list(authorsbooks.keys())[6]
authorsbooks[seventh_author] = "Updated Book"

sixth_author = list(authorsbooks.keys())[5]
del authorsbooks[sixth_author]

last_key_value_pair_authors = list(authorsbooks.items())[-1]