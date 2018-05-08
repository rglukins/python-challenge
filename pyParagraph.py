import os
import re

#create a file path to access the text file
file_path = os.path.join(".", "paragraph_1.txt")

def file_loader(filepath):   #do I even need this?
    """Extract the text data from the paragraph file"""
    with open(filepath, "r") as paragraph_file_handler:
        return paragraph_file_handler.read().lower().split()

def word_count(file_text):
    return int(len(file_text))
     

paragraph_text = file_loader(file_path)
#print(paragraph_text)
#print(len(paragraph_text))
print("Approximate word count: " + str(word_count(paragraph_text)))