def matrix():
    m = int(input('Write m rows: '))
    n = int(input('Write n columns: '))
    a = [None] * m
    for row in range(m):
        a[row] = [None] * n
        for column in range(n):
            a[row][column] = float(input('A = ['+str(row + 1)+'],['+str(column + 1)+'] --> '))
    return a, m, n
    
def result(a, m, n):
    print('{}'.format('\nMatrix\n'))
    for row in range(m):
        for column in range(0, n):
            print('{:>2.2f} | '.format(a[row][column]), end=' ');
        print('\n''\t')
    return

#Main
a, m, n = matrix()
result(a, m, n)