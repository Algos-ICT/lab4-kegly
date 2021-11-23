def push(a, x):     # добавление элемента на вершину стека
    global top
    top += 1
    a[top] = x

def pop(a):     # удаление элемента
    global top
    x = a[top]
    a[top] = None
    top -= 1
    return x



f = open('input.txt')
m = int(f.readline())   # количество команд
arr = [None]*m
top = -1
arr_pop = []    # массив с извлеченными элементами


for i in range(m):
    oper = f.readline().rstrip()    # удаление \n в конце

    if oper == '-':
        arr_pop += [pop(arr)]
    else:
        push(arr, int(oper[1:]))
file = open('output.txt', 'w')
for i in arr_pop:
    file.write(str(i)+'\n')
