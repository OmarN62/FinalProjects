spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
    output = ''
    for i in range(len(list)):
        if len(list)-1 == i:
            output += 'and ' + list[i]
        else:
            output += list[i] + ', '
    return output

result = comma(spam)
print(result)