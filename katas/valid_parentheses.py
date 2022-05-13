def valid_parentheses(string):
    #your code here
    i = 0
    opened, flag = 0, 0
    list = []
    if 0 <= len(string) <= 100:
        while i < len(string):
            if ord(string[i]) == 40 or ord(string[i]) == 41:
                list.append(string[i])
            i+=1
        for i in list:
            if i == '(':
                opened +=1
                flag += 1
            if i == ')' and flag == 0:
                return False
            if i == ')' and flag >= 1:
                opened -=1
                flag -= 1
        if opened == 0:
            return True
    return False
