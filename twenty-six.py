word = input("Type in any word: ")

if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    print(word+"way")
else:
    new_word = word[1:]+word[0]+"ay"
    print(new_word.lower())