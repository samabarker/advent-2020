inputt = '''((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''

inputz = list(inputt.split('\n'))

def get_pairs(inputz):
    pairs = []
    for i in range(0,len(inputz)):
        if inputz[i] == "(":
            counter = 1
            for j in range(i+1, len(inputz)):
                if inputz[j] == "(":
                    counter +=1
                elif inputz[j] == ")":
                    counter -= 1
                    if counter == 0:
                        pairs.append((i,j))
                        break
    return pairs


def calculate(equation):
    equation_list = list(equation.split(' '))
    running_total = 0
    for i in range(1,len(equation_list) - 1,2):
        if i == 1:
            running_total =int(equation_list[0])
        if equation_list[i] == "+":
            running_total += int(equation_list[i+1])
        elif equation_list[i] == "*":
            running_total *= int(equation_list[i+1])
    return running_total


def replace(strng, loc, replacement):
    new_str = strng[:loc[0]-1] + str(replacement) + strng[loc[1]+1:]
    return new_str



answers = []
for j in inputz:
    for i in range(0,20):
        if ")" not in j:
            break
        paranth = get_pairs(j) 
        for i in paranth:
            if "(" not in j[i[0]+1:i[1]] and ")" not in j[i[0]+1:i[1]]:
                if "+" in j[i[0]+1:i[1]] or "*" in j[i[0]+1:i[1]]:
                    numb = calculate(j[i[0]+1:i[1]])
                    j = replace(j, [i[0]+1,i[1]], numb)
                    break
    answers.append(calculate(j))
        
print(sum(answers))