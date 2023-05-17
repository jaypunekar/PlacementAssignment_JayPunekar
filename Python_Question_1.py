#Take Input
string = input("Enter a String: ")

#Convert it to a List for easier iteration
string = string.split()

# Add all the words to a dictionary and initialize thier value to 0
word_dict = {}
for word in string:
    word_dict[word] = int(0)

#Increment the value whenever a word is spotted
for word in string:
    word_dict[word] = word_dict[word] + 1

#List of most frequently occuring words in case there are more than one
most_frequent = list()

#Keymax stores the word whose occurance is the most frequent
Keymax = max(word_dict, key= lambda x: word_dict[x])

#Finding other words(if exist) with the highest frequency
for value, key in word_dict.items():
    if key == word_dict[Keymax]:
        most_frequent.append(value)

#Printing the most frequent word/words
if len(most_frequent) == 1:
    print(f'The most frequently occuring word is "{most_frequent[0]}" and its frequency is "{word_dict[most_frequent[0]]}"')
else:
    print(f'The most frequently occuring words are "{most_frequent}" and their frequency is "{word_dict[Keymax]}"')


