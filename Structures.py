#Alinea Grace Del Mundo
#Structure


letters = ['e','l','l','e','n','e','l','a',
                'g','i','n','g','n','a','i','i',
                'w','a','n','s','a','o','u',
                't','i','n','g',]


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(5)
print ("letters repeated")
print(repeat)
