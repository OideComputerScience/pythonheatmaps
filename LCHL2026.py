def calculate_readability_score(text):
    
    #Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)
    
    #Initialise the word counters
    word_count = len(words) # Number of words in list
    short_words_count = 0
    for i in range(word_count):
        if len(words[i]) <3:
            short_words_count +=1
    print("Short Words:", short_words_count)
    #Initialise the number of sentences
    sentence_count = text.count(".") + text.count("!")
    
    #Calculate the readability score
    #score = word_count * sentence_count
    
    score = 0.4 *((word_count/sentence_count) + 100 * ((word_count-short_words_count)/word_count))
    score = round(score, 2) # Round the score to 2 d.p.
    complex_count = 0
    complex_words = 0 
    for j in range(word_count):
        for k in words[j]:
            if k == 'a' or k == 'A' or k=='E' or k== 'e' or k== 'i' or k == 'I' or k == 'o' or k =='O' or k == 'u' or k == 'U':
                complex_count +=1
        if k[-1] == 'e':
            complex_count -= 1
        if complex_count >= 3:
            complex_words +=1
        complex_count = 0
    
    #complex_words = complex_count - 1
    print("Complex Words:", complex_words)
    return score

#Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

#Calculate the score for text1
score1 = calculate_readability_score(text1)
print("Readability score 1:", score1)
print("\n")
#Calculate the score for text1
score2 = calculate_readability_score(text2)
print("Readability score 2:", score2)

print("\n")
if score1 < score2:
    print("The first text is easier to read")
elif score2 < score1:
    print("The second text is easier to read")
    