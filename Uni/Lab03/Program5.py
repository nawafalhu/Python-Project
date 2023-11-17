# Oppenheimer is good movie for Ali or not
Ali = set(["Inception", "Life of Pi", "The dark knight", "A Separation"])
Nawaf= set(["The dark knight", "12 Angry men", "Inception", "LOR:TT"])
Mohammed = set(["LOR:TT", "Seven Samurai", "Inception", "The Matrix"])

Ali_and_nawaf = Ali.intersection(Nawaf)
Ali_and_Mohammed = Ali.intersection(Mohammed)

if len(Ali_and_nawaf) > len(Ali_and_Mohammed) : 
    print('Oppenheimer is good movie for Ali')
else :
    print("Oppenheimer is not good movie for Ali")