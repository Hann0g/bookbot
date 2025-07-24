def count_words(text):
  """
  Counts the number of words in a given string.

  Args:
    text: The input string (e.g., the content of a book).

  Returns:
    The number of words in the string.
  """
  words = text.split()
  return len(words)

# --- How to read your .txt file and then count the words ---

file_path = ".gitignore/books/frankenstein.txt" # Make sure this path is correct for your file

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        book_content = file.read() 
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    book_content = "" 
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    book_content = ""


if book_content: 
    num_words = count_words(book_content)

    print(f"{num_words} words found in the document")
else:
    print("Could not process word count due to file reading error.")