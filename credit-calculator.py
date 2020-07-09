import math
import argparse

# Differentiated Payment
def diff_payment(credit_principal, months, nominal_interest, current_period):
    return math.ceil((credit_principal / months) + (nominal_interest * (credit_principal - ((credit_principal * (current_period - 1)) / months))))

# Calculate Nominal Interest
def calculate_nominal_interest(credit_interest):
    return credit_interest / (12 * 100)

# Calculate Number of Payments
def calculate_n_payments(credit_principal, monthly_payment, nominal_interest):
    return math.log(monthly_payment / (monthly_payment - (nominal_interest * credit_principal)), 1 + nominal_interest)

# Calculate Annuity
def calculate_annuity(credit_principal, nominal_interest, months):
    return int(math.ceil(credit_principal * ((nominal_interest * math.pow(1 + nominal_interest, months)) / (math.pow(1 + nominal_interest, months) - 1))))

# Calculate Credit Principle
def calculate_credit_principle(monthly_payment, nominal_interest, months):
    return round(monthly_payment / ((nominal_interest * math.pow(1 + nominal_interest, months)) / (math.pow(1 + nominal_interest, months) - 1)))

# Command Line Argument Parsing
parser = argparse.ArgumentParser()

# --type
parser.add_argument('--type')

# --principal
parser.add_argument('--principal')

# --periods
parser.add_argument('--periods')

# --payment
parser.add_argument('--payment')

# --interest
parser.add_argument('--interest')

# Parse passed arguments
args = parser.parse_args()


# Args data
action = args.type
credit_principal = int(args.principal) if args.principal != None else None
months = int(args.periods) if args.periods != None else None
credit_interest = float(args.interest) if args.interest != None else None
monthly_payment = int(args.payment) if args.payment != None else None

# String to be printed at end
string = ''

# Validate User Action
if action != 'diff' and action != 'annuity':
    print('58 Incorrect parameters')


# Diff
if action == 'diff':
    if monthly_payment != None or credit_principal == None or months == None or credit_interest == None:
        print('64 Incorrect parameters')
    else:
        paid = 0

        for count in range(1, months + 1):
            difference_payment = diff_payment(credit_principal, months, calculate_nominal_interest(credit_interest), count)
            paid += difference_payment
            string += 'Month {}: paid out {}\n'.format(count, difference_payment)

if action == 'annuity':
    if (credit_principal != None and months != None) or (credit_principal != None and (monthly_payment == None or credit_interest == None) or (months != None and (monthly_payment == None or credit_interest == None))):
        print('77 Incorrect parameters')

    elif credit_principal != None:
        nominal_interest = calculate_nominal_interest(credit_interest)
        months = calculate_n_payments(credit_principal, monthly_payment, nominal_interest)

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
        paid = int(months * monthly_payment)
        string += '\n'
    elif months != None:
        nominal_interest = calculate_nominal_interest(credit_interest)
        credit_principal = calculate_credit_principle(monthly_payment, nominal_interest, months)
        string = 'Your credit principal = {}!'.format(credit_principal)
        paid = int(months * monthly_payment)
        string += '\n'

string += '\nOverpayment = {}'.format(paid - credit_principal)

print(string)