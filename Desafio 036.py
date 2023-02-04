value = float(input('Type the value of the house: '))
salary = float(input('Type your salary: '))
financing = float(input('How many years of financing?:'))
print('House value : {}'.format(value))
print('Salary: {}'.format(salary))
print('Financing years: {}'.format(financing))
render_monthly = value/(financing*12)
if render_monthly > salary*30/100:
    print('The loan was approved')
else:
    print('Your loan was denied')