#reverser function

from ctypes.wintypes import WORD


# def backwards(word): 
# word = input("What word do you want to be reversed?")
# for index in range(len(word) -1, -1, 11):
#     word += word[index]

    
# print(input)

reversed_word = input("What word would you like to reverse?")


def reverser(word):
    reversed_word = ""
    for index in range(len(word)-1, -1, -1):
        reversed_word += word[index]
    return reversed_word

print(f"Your word reversed is: {reverser(reversed_word)}")
