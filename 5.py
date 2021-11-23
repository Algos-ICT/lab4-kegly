def push(a, x):     # добавление элемента на вершину стека
    global top
    top += 1
    a[top] = x
    if top == 0:
        max_stack[0]=x
    else:
        max_stack.append(max(max_stack[top-1], x))

def pop(a):     # удаление элемента
    global top
    x= a[top]
    a[top] = None
    max_stack.pop()
    top -= 1
    return x


f = open('input.txt')
m = int(f.readline())
top = -1
stack=[None] * m
max_stack=[0]
file= open('output.txt', 'w')
for i in range(m):
    oper = f.readline().rstrip()    # удаление \n в конце

    if oper == 'pop':
        pop(stack)

    elif oper == 'max':
        file.write(str(max_stack[-1])+'\n')

    else:
        push(stack, int(oper[5:]))





