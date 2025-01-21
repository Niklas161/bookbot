book_path = "books/frankenstein.txt"

def main():
  text = get_book_text(book_path)
  print(text)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words():
  text = get_book_text(book_path)
  woerter = text.split()
  anzahl_woerter = len(woerter)
  print(anzahl_woerter)

count_words()