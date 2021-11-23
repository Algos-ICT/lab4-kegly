f = open('input.txt')
count=int(f.readline()) # количество последовательнотей

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
                    return False
            elif i == ']':
                if stack[top] == '[':
                    pop(stack)

                else:
                    return False
            elif i == '}':
                if stack[top] == '{':
                    pop(stack)
                else:
                    return False
    if top != -1:
        return False
    return True
file = open('output.txt', 'w')

for line in range(count):
    if check(line):
        file.write('YES\n')
    else:
        file.write('NO\n')