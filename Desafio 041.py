hyp = float(input('Type the height of hypotenuse: '))
adj = float(input('Type the height of adjcent: '))
opp = float(input('Type the height of opposite: '))
if hyp < adj + opp and adj < hyp + opp and opp < hyp + adj:
    print('This straight can form a triangle')
else:
    print('This is not a triangle')
if hyp == adj == opp:
    print('This triangle is equilateral')
elif adj == opp:
    print('This triangle is isosceles')
elif hyp != adj and hyp != opp and adj != opp:
    print('This triangle is escaleno')