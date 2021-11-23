def push(a, x):
    global tail

    a[tail] = x
    if tail == len(a)-1:
        tail = 0

    else:
        tail += 1



def pop(a):     # удаление элемента
    global head
    x = a[head]
    a[head] = None
    if head == len(arr)-1:
        head = 1
    else:
        head += 1
    return x


f = open('input.txt')
m = int(f.readline())   # количество команд
arr = [None]*m
head= 0
tail= 0
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
