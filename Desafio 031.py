trip = float(input('Type the range of your trip in km: '))
if trip <= 200:
    print('Your ticket cost {:.2f}'.format(trip*0.5))
else:
    print('Your ticket cost {:.2f}'.format(trip*0.45))