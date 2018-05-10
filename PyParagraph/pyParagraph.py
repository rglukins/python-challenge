import os
import re
import string

#create a file path to access the text file
file_path = os.path.join(".", "paragraph_2.txt")

# create useful functions for loading files & doing calculations
def file_loader(filepath):   
    """Extract the text data from the paragraph file"""
    with open(filepath, "r") as paragraph_file_handler:
        return paragraph_file_handler.read().lower().split()

def word_count(file_text):
    return int(len(file_text))

#get the text from the file
paragraph_text = file_loader(file_path)

#For Approximate Letter Count
cleaned_text = []   #clear the punctuation for the the ends of the strings in the text list
for word in paragraph_text:
    word = str(word)
    word = word.strip(string.punctuation)
    cleaned_text.append(word)

char_count = 0  # create a variable for counting characters (for average word length)
for i in cleaned_text:      #count the number of characters in the cleaned word list
    chars_in_word = len(str(i))
    char_count = char_count + chars_in_word
av_letter_count = char_count / len(paragraph_text) #For Average Letter Count: create variable for average letter coun
 

#Identify Individual sentences
with open(file_path, "r") as text_file:
    paragraph = text_file.read()
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)

#create variable for sentence count
sentence_count = len(sentences)

#create variable for words per sentence
av_words_per_sentence = word_count(paragraph_text) / sentence_count


#print outputs
print("Approximate word count: " + str(word_count(paragraph_text)))
print (f'Approximate Sentence Count {sentence_count}')
print(f'Average letter Count: {av_letter_count}')
print(f'Average Words Per Sentence: {av_words_per_sentence}')


