def get_even_list(l) :
    get_even = []
    for i in l :
        if i % 2 ==0 :
            get_even.append(i)
    return get_even
x = int(input('Số phần tử: '))
l = []
for i in range(x) :
    y = int(input('Nhap :'))
    l.append(y)
print(get_even_list(l))