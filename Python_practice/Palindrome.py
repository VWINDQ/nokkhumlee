# Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

a = "qazxccxzaq"
i,j = 0 ,len(a) - 1

is_palindrome = True
while i < j:
    if a[i] != a[j]:
        is_palindrome = False
        break
    i += 1
    j -=1

if is_palindrome:
    print('yes')
else:
    print('no')
