booksauthor = {
    "The Road": "Cormac McCarthy",
    "The Handmaid's Tale": "Margaret Atwood",
    "Dune": "Frank Herbert",
    "The Alchemist": "Paulo Coelho",
    "The Catch-22": "Joseph Heller",
    "Frankenstein": "Mary Shelley",
    "The Kite Runner": "Khaled Hosseini",
    "The Hunger Games": "Suzanne Collins",
    "Harry Potter and the Sorcerer's Stone": "J.K. Rowling",
    "One Hundred Years of Solitude": "Gabriel Garcia Marquez",
    "The Shining": "Stephen King",
    "The Color Purple": "Alice Walker"
}

entire_dict_books = booksauthor

ninth_book = list(booksauthor.keys())[8]
ninth_book_author = booksauthor[ninth_book]

fifth_book = list(booksauthor.keys())[4]
booksauthor[fifth_book] = "Updated Author"

third_book = list(booksauthor.keys())[2]
del booksauthor[third_book]

last_key_value_pair_books = list(booksauthor.items())[-1]