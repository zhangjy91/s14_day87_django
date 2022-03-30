def add(x,y):
    return x + y

def div(x,y):
    return x/y

def test_a(x,y):
    final = add(x,y) - div(x,y)
    print(final)

if __name__ == '__main__':
    print('aaaaaaa')

    temp_a = add(5,6)
    print(temp_a)

    temp_b = div(10,2)
    print(temp_b)

    test_a(temp_a,temp_b)