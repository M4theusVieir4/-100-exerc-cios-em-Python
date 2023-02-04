note1 = float(input('Type your first note:'))
note2 = float(input('Type your second note:'))
media = (note1 + note2)/2
if media < 5:
    print('disapproved')
elif media > 5 and media < 6.9:
    print('recovery')
elif media > 7:
    print('Approved')