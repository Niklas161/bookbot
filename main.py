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
  return anzahl_woerter

def count_characters():
  chars_amount = {}
  text = get_book_text(book_path)
  lower_text = text.lower()
  for zeichen in lower_text:
    if zeichen.isalpha():
      if zeichen in chars_amount:
        chars_amount[zeichen] += 1
      else:
        chars_amount[zeichen] = 1
  return chars_amount

def sort_on(dict):
  return dict["num"]


word_count = count_words()
char_count = count_characters()

chars_list = []
for char, count in char_count.items():
  chars_list.append({"char": char, "num": count})

chars_list.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f'{word_count} words found in the document')

for item in chars_list:
  print(f"The '{item['char']}' character was found {item['num']} times")

print("--- End report ---")