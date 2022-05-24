year = int(input())

magic = 400
if year % magic == 0 or (year % 4 == 0 and year % 100 != 0):
    print('Leap')
else:
    print('Ordinary')
