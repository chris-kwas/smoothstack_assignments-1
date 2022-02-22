import re

#function for palindrome in coding exercise 3:
def is_palindrome(text):
    text = text.lower()
    text = "".join(re.findall("[a-z]", text))
    for x in range(0, int(len(text) / 2) + 1):
        if text[x] is not text[-(x + 1)]:
            print("N")
            return
    print("Y")
    return

if __name__ == '__main__':
    #start of coding exersice 3:
    print("Hello World"[8])
    string = "thinker"
    answer = slice(2, 5, 1)
    print(string[answer])
    
    #S=’hello’,what is the output of h[1]
    #answer = e
    #S=’Sammy’ what is the output of s[2:]”
    #answer = mmy
    
    #With a single set function can you turn the word ‘Mississippi’ to distinct character word.
    word = "".join(set("Mississippi"))
    print(word)

    input_line_amt = int(input())
    phrases = list()
    for x in range(input_line_amt):
        text_line = input()
        phrases.append(text_line)
    for phrase in phrases:
        is_palindrome(phrase)




