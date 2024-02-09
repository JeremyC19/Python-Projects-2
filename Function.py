
def reverse_char(string):
    string = "".join(reversed(string))
    return string


def reverse_words():
    print("Enter three words you want to reverse the order of characters: ")

    s1 = input()
    s2 = input()
    s3 = input()

    r1 = reverse_char(s1)
    r2 = reverse_char(s2)
    r3 = reverse_char(s3)

    print("")
    print("Original words: ")
    print(s1 + " " + s2 + " " + s3)
    print("Reversed words: ")
    print(r3 + " " + r2 + " " + r1)


reverse_words()
