n1 = float(input('Type your first grade: '))
n2 = float(input('Type your second grade: '))
average = (n1+n2)/2
print('Your average is {:.1f}'.format(average))
if average >=6.0 :
    print('Your grade is good, Congratulation!')
else:
    print('Your grade is bad,study more!')