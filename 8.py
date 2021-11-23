import operator

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul}

def postfi(srt):
    stack = []
    l=list(srt.split())
    for i in l:
        if i.isdigit():
            stack.append(i)

        else:
            a, b = stack.pop(), stack.pop()
            stack.append(OPERATORS[i](int(b), int(a)))

    return stack.pop()


f = open('input.txt')
m = int(f.readline())
line= f.readline()
file= open('output.txt', 'w')
file.write(str(postfi(line)))