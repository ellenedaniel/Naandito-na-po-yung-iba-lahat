#Ellene Gay S. Daniel
#Palindrome



def isPalindrome():
    string = input('Enter a string: ')
    string1 = string[::-1]
    if string[0] == string[(len(string)-1)] and string[1:(len(string)-2)] == string1[1:(len(string)-2)]:
            print('It is a palindrome')
    else:
        print('It is not a palindrome')
isPalindrome()
