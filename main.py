def main():
    contents = book_contents("books/frankenstein.txt")
    word_count = number_words(contents)
    characters = number_characters(contents)
    report_list = report(characters, word_count)

    
    
    print(report_list)
    
    

def report(count, word_count):
    char_sort = []
    for char, count in count.items():
        if char.isalpha():
            char_sort.append({"char": char, "num": count})
    
    def sort_on(char_sort):
        return char_sort["num"]
    
    char_sort.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_data in char_sort:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")

    print("--- End report ---")



    
def number_characters(book):
    character_count = {}
    lower_case = book.lower()
    for characters in lower_case:
        if characters not in character_count:
            character_count.update({characters: 1})
        else:
            character_count[characters] += 1
    return character_count
       



def number_words(text):
    return len(text.split())
        


def book_contents(path):
    with open(path) as f:
        return f.read()
    
main()
