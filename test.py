# Question 1
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print("Book not found.")
    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("Available books:")
            for book in self.books:
                print(book)
library = Library()
book1 = Book("Book1", "Book2", "Book3")
book2 = Book("1984", "Auth2", "67890")
library.add_book(book1)
library.add_book(book2)
library.display_books()
library.remove_book("12345")
library.display_books()


# Question 2
import pandas as pd 
 
data = { 
    'Product': ['A', 'B', 'A', 'C', 'B', 'C'], 
    'Sales': [100, 200, 150, 300, 250, 400], 
    'Region': ['North', 'South', 'North', 'East', 'South', 'East'] } 
 
df = pd.DataFrame(data)  
 
total_sales = df.groupby('Product')['Sales'].sum()
print("Total Sales per Product:\n", total_sales)

highest_sales = df.groupby('Region')['Sales'].max()
print("\nHighest Sales per Region:\n", highest_sales)

df['Discounted Price'] = df['Sales'] * 0.9
print("\nUpdated DataFrame:\n", df)


# question 3
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words[::-1]:  
        reversed_words.append(word)
    return " ".join(reversed_words)
input_string = "Python is great"
output_string = reverse_words(input_string)
print(output_string)


# Question 4
def find_missing_number(arr):
    n = len(arr) + 1 
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)
    return expected_sum - actual_sum


numbers = [1, 2, 4, 5, 6]
missing_number = find_missing_number(numbers)
print(missing_number)


# Question 5
import threading

def sum_of_squares(start, end, result, index):
    result[index] = sum(i * i for i in range(start, end + 1))

def parallel_sum_of_squares(n, num_threads=2):
    step = n // num_threads
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i != num_threads - 1 else n
        thread = threading.Thread(target=sum_of_squares, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)

# input
n = 10
print(parallel_sum_of_squares(n))
