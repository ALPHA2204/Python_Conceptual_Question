'''
A list of words given to you as a part of the prefix Code.
Print the longest word in the Word . If there are multiple words with the same Word with the same size .
Print the one which appears at the rightmost end of the list'''

l =input().split(",")
maxword , maxlen = "",0
for word in l:
    if len(word)>=maxlen:  # If you would use not use equal to then this is going to print  ..By useing ">=" then we get right most word towards ends.
        maxlen=len(word)
        maxword = word
print(maxword)
    