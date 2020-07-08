import math

print('What do you want to calculate?')
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
action = input()



if action == 'n':
    credit_principal = int(input('Enter the credit principal: '))
    monthly_payment = int(input('Enter monthly payment: '))
    nominal_interest = float(input('Enter credit interest: ')) / (12 * 100)

    months = math.log(monthly_payment / (monthly_payment - (nominal_interest * credit_principal)), 1 + nominal_interest)

    if months % 1 != 0:
        months = math.ceil(months)

    year = months // 12
    month = months % 12
    if month == 1:
        month_string = 'month'
    else:
        month_string = 'months'

    if year == 1:
        year_string = 'year'
    else:
        year_string = 'years'
        
    if year == 0:
        string = 'You need {} {} to repay this credit!'.format(month, month_string)
    elif month == 0:
        string = 'You need {} {} to repay this credit!'.format(year, year_string)
    else:
        string = 'You need {} {} and {} {} to repay this credit!'.format(year, year_string, month, month_string)

elif action == 'a':
    credit_principal = int(input('Enter the credit principal: '))
    months = int(input('Enter count of periods: '))
    nominal_interest = float(input('Enter credit interest: ')) / (12 * 100)

    annuity = int(math.ceil(credit_principal * ((nominal_interest * math.pow(1 + nominal_interest, months)) / (math.pow(1 + nominal_interest, months) - 1))))

    string = 'Your annuity payment = {}!'.format(annuity)
elif action == 'p':
    monthly_payment = float(input('Enter monthly payment: '))
    months = int(input('Enter count of periods: '))
    nominal_interest = float(input('Enter credit interest: ')) / (12 * 100)
    credit_principal = round(monthly_payment / ((nominal_interest * math.pow(1 + nominal_interest, months)) / (math.pow(1 + nominal_interest, months) - 1)))

    string = 'Your credit principal = {}!'.format(credit_principal)

print(string)