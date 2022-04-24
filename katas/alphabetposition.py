def alphabet_position(text):
    text = text.lower()
    s = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if i != 0:
                s += " "
            s += str(ord(text[i]) - 96)
    return s

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

# best solve:
# def alphabet_position(text):
#    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# absurd C solve: (Test Crashed: Caught unexpected signal: SIGSEGV (11). Invalid memory access)
# it actually works, but I don't know how to solve this problem
# char *alphabet_position(const char *text)
# {
# 	int i = 0, j = 0, count = 0, flag = 0, n = 0;
# 	int chars = 0;
# 	char *str;
# 	while(text[i])
# 		i++;
# 	for (j = 0; j < i; j++)
# 	{
# 		flag = 0;
# 		if (text[j] >= 65 && text[j] <= 90)
# 		{
# 			count = text[j] - 64;
# 			if (count < 10)
# 				chars += 1;
# 			else
# 				chars += 2;
# 			flag++;
# 		}
# 		else if (text[j] >= 97 && text[j] <= 122)
# 		{
# 			count = text[j] - 96;
# 			if (count < 10)
# 				chars += 1;
# 			else
# 				chars += 2;
# 			flag++;
# 		}
# 		if (flag == 1 && j != i - 1)
# 			chars++;
# 	}
# 	if (chars == 0)
# 		return "";
# 	str = malloc(sizeof(char) * chars + 1);
# 	flag = 0;
# 	for (j = 0; j < i; j++, n++)
# 	{
# 		if (text[j] >= 65 && text[j] <= 90)
# 		{
# 			if (flag == 1)
# 				str[n] = ' ', n++;
# 			count = text[j] - 64;
# 			if (count < 10)
# 				str[n] = count + 48;
# 			else
# 			{
# 				str[n] = (count / 10) + 48;
# 				n++;
# 				str[n] = (count % 10) + 48;
# 			}
# 			flag = 1;
# 		}
# 		else if (text[j] >= 97 && text[j] <= 122)
# 		{
# 			if (flag == 1)
# 				str[n] = ' ', n++;
# 			count = text[j] - 96;
# 			if (count < 10)
# 				str[n] = count + 48;
# 			else
# 			{
# 				str[n] = (count / 10) + 48;
# 				n++;
# 				str[n] = (count % 10) + 48;
# 			}
# 			flag = 1;
# 		}
# 		else
# 		{
# 			n--;
# 		}
# 	}
# 	str[chars] = '\0';
# 	return str;
# }