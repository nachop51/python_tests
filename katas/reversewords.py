def space_count(text):
    count = 0
    i = 0
    if len(text) == 0:
        return 0
    while text[i] == " ":
        count += 1
        i += 1
    return count

def reverse_words(text):
    reverse = ""
    for t in text.split():
        reverse += t[::-1]
        text = text[len(t):]
        spaces = space_count(text)
        reverse += (" " * spaces)
        if spaces != 0:
            text = text[spaces:]
    return reverse

print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('double  spaced  words'))