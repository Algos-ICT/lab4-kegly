f = open('input.txt')
count=f.readline() # количество последовательнотей
line = f.readline()

top = -1
def push(a, x):     # добавление элемента на вершину стека
    global top
    a[top+1] = x
    top += 1


def pop(a):     # удаление элемента
    global top
    a[top] = None
    top -= 1



def check(line):
    stack = [None]*len(line)
    if line=='':
        return True
    if line[0] in '}])': # если начинается с закрывающей
        return False
    for i in line:
        if i in '[({':
            push(stack, i)
        else: # если скобка закрывающая
            if i == ')':
                if stack[top] == '(':  # если для нее есть открывающая пара
                    pop(stack)
                else:
                    return line.index(i)+1
            elif i == ']':
                if stack[top] == '[':
                    pop(stack)

                else:
                    return line.index(i)+1
            elif i == '}':
                if stack[top] == '{':
                    pop(stack)
                else:
                    return line.index(i)+1
    if top != -1:
        return line.index(stack[0])+1
    return 'Succsess'
file = open('output.txt', 'w')

file.write(str(check(line)))