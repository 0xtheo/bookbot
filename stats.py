def word_count(string):
    words = string.split()
    num_words =  len(words)
    print(f"Found {num_words} total words")

def letter_count(string):
    freq = {}
    for letter in string:
        letter = letter.lower()
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq

def sort_on(dict):
    return dict["num"]

def sort_letter_freq(letters_dict):
    letters_list = []
    for letter_count in letters_dict:
        letters_list.append({"char" : letter_count, "num" : letters_dict[letter_count]})

    letters_list.sort(reverse=True, key=sort_on)
    return letters_list

    # print(letters_list)
    
    