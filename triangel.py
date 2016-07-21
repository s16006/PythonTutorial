h = int(input('高さを入力してください')) 
a=[]

for i in range(h+1):
    a.append(i)

for o in a:
    print(o*'*',end=' ')
    print()

"""
for horizontal in range(h + 1):
    for vertical in range(horizontal):
        if vertical == 0 or vertical == horizontal - 1\
                or horizontal == h:
            print('*', end='')
        else:
            print('+', end='')

        print()
"""
'''

*
**
*+*
*++*
*****

'''
for vertical in range(h + 1):
    for vertical in range(vertical):
        if horizontal == 0 or horizontal == vertical - 1\
                or vertical == h:
            print('*', end='')
        else:
            print('+', end='')

        print()
