word = input("Enter a word to find out if it is a Palindrome")
def isPalindrome(s):
    rev= "".join(reversed(s))
    if (s == rev):
        return True
    else:
        return False

ans = isPalindrome(word)

if (ans == True):
    print("Yes")
else:
    print("No")
