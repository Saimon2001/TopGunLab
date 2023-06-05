#ex2 Create a Python program that reads a text file and counts the occurrences of each word using a dictionary. The program should print the words and their counts.
import re

def read_count():
    texto = str(input("write the name of the txt file that you need to count the occurrences>"))
    with open(texto, "r") as file:
        contents = file.read()
        print(contents)
    
    word_counts = {}
    palabras = re.findall(r'\b\w+\b', contents.lower())
    for word in palabras:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    for word, count in word_counts.items():
        print(f"{word}:{count}")
    

read_count()   