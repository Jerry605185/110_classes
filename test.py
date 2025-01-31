def palindrome(word:str,left=0,right=0):
    right = len(word)-1
    if(word == "" or len(word) == 1):
        return True
    if(word[left] != word[right]):
        return False
    return palindrome(word,left+1,right-1)
word = "a"
palindrome(word)