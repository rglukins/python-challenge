import string
import re
import os

#create a file path to access the text file
file_path = os.path.join(".", "paragraph_1.txt")

with open(file_path, "r") as text_file:
    paragraph = text_file.read()
#print(paragraph)

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)
#print(sentences)

#create variable for sentence count
sentence_count = len(sentences)
print(sentence_count)
print (f'Approximate Sentence Count {sentence_count}')