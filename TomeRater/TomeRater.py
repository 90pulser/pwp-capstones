class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "User address has been updated."

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", books read: " + len(self.books)

    def __eq__(self, other_user):
        if other_user.name == self.name and other_user.email == self.email:
            self = other_user

    def read_book(self, book, rating):
        rating = none
        self.books[book] = rating

    def get_average_rating(self, book):
        rated_average = 0
        for book in self.books:
            rated_average += self.books[book]
        return rated_average / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

    def add_rating(self, rating):
        if (rating >= 0 and rating <= 4):
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def get_average_rating(self, rating):
        rate_average = 0
        for rating in self.ratings:
            rate_average += self.ratings[rating]
        return rate_average / len(self.ratings)

    def __eq__ (self, other_book):
        if other_book.title == self.title and other_book.isbn == self.isbn:
            self = other_book

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(Book, author):
        self.title = title
        self.isbn = isbn
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(Book, subject, level):
        self.title = title
        self.isbn = isbn
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        created_book = Book(title, isbn)
        return created_book

    def create_novel(self, title, author, isbn):
        created_novel = Fiction(title, author, isbn)
        return created_novel

    def create_non_fiction(self, title, subject, level, isbn):
        created_non_fiction = Non_Fiction(title, subject, level, isbn)
        return created_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        rating = 0
        if email in self.users:
            User.read_book(book, rating)
            Book.add_rating(rating)
            if book in self.books.keys:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with email " + email + "!"

    def add_user(self, name, email, user_books = None):
        user_books = [None]
        new_user = User(name, email)
        if len(user_books) > 0:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys:
            return self.books[book]

    def print_users(self):
        for user in self.users.values:
            return self.users[user]

    def most_read_book(self):
        most_read = ""
        times_read = 0

        for book in self.books:
            if self.books.values[book] > times_read:
                most_read = self.books[book]
                times_read = self.books.values[book]
        return most_read

    def highest_rated_book(self):
        highest_rated = ""
        highest_rating = 0
        for book in self.books:
            if book.get_average_rating[book] > highest_rating:
                highest_rated = book
                highest_rating = book.get_average_rating[book]
            return highest_rated

    def most_positive_user(self):
        positive_user = ""
        positive_score = 0
        for user in self.users:
            for book in User.books:
                 if User.books.values[book]/len(User.books) > positive_score:
                     positive_score = User.books.values[book]
                     positive_user = user
        return positive_user
