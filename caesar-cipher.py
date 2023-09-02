alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encryot(text2, shift2) :
    new_word = ""
    for letter in text2 :
        index = alphabet.index(letter)
        new_index = index + shift2
        new_letter = alphabet[new_index]
        new_word += new_letter
    print(new_word)

def decode(text3, shift3) :
    new_word = ""
    for letter in text3 :
        index = alphabet.index(letter)
        new_index = index - shift3
        new_letter = alphabet[new_index]
        new_word += new_letter
    print(new_word)

def caesar(cas_text, cas_shift, cas_dir) :
    new_word = ""
    for letter in cas_text :
        index = alphabet.index(letter)
        if cas_dir == "decode" :
            index * -1
        new_index = index + cas_shift
        new_letter = alphabet[new_index]
        new_word += new_letter
    print(new_word)


if direction == "encode" :
    encryot(text, shift)
elif direction == "decode": 
    decode(text, shift)
else : 
    print("Try again")