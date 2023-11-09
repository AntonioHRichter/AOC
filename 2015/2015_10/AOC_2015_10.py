input = '3113322113'

def lookAndSay(input):
    result = ''
    i = 0
    while i < len(input):
        for l in range(0, len(input) - i):
            if i == len(input) - 1:
                result += str(1) + input[i]
                i += 1
                break
            if input[i+l] != input[i]:
                result += str(l) + input[i]
                i += l
                break
    return result

for i in range(0, 51): 
    print(i,': ',len(input))
    input = lookAndSay(list(input))

