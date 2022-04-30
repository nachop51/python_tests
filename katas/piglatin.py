def pig_it(text):
    #your code here
    l = text.split()
    print(l)
    s = ""
    for v, i in enumerate(l):
        if i.isalpha():
            if v != 0: s += " "
            s += i[1:] + i[:1] + "ay"
        else:
            if v != 0: s += " "
            s += i
    return s

print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it('O tempora o mores !'))