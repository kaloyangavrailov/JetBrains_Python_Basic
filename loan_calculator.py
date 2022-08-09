import argparse
import math
activator = False
parser = argparse.ArgumentParser(description="testest")
parser.add_argument("--type", choices=["annuity","diff"], required=True, help="Incorrect parameters.")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal",type=int)
parser.add_argument("--periods",type=int)
parser.add_argument("--interest",type=float)

args = parser.parse_args()

if args.interest:
    if args.type == 'diff':
        if args.payment:
            print(f'Incorrect parameters.')
        else:
            if args.principal and args.periods and args.interest:
                if args.principal > 0 and args.periods > 0:
                    i = (args.interest / 12) / 100
                    p = args.principal
                    n = args.periods
                    total_payments = 0
                    for m in range(1, n + 1):
                        payment = math.ceil(p/n + i * (p-((p*(m-1))/n)))
                        total_payments += payment
                        print(f'Month {m}: payment is {payment}')
                    overpayment = total_payments - p
                    print()
                    print(f'Overpayment = {overpayment}')
                else:
                    print(f'Incorrect parameters.')
            else:
                print(f'Incorrect parameters.')
    else:
        if args.principal and args.periods and args.interest:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                i = (args.interest / 12) / 100
                n = args.periods
                p = args.principal
                annuity = math.ceil(p * ((i * (1 + i)**n)/(((1+i)**n)-1)))
                overpayment =(annuity*n) - p
                print(f'Your annuity payment = {annuity}!')
                print(f'Overpayment = {overpayment}')
            else:
                print(f'Incorrect parameters.')
        elif args.payment and args.periods and args.interest:
            if args.payment > 0 and args.periods > 0 and args.interest > 0:
                i = (args.interest / 12) / 100
                a_p = args.payment
                n = args.periods
                principal = (a_p / ((i*(1+i)**n)/(((1+i)**n)-1)))
                overpayment = ((a_p*n) - principal)
                print(f'Your loan principal = {int(principal)}!')
                print(f'Overpayment = {math.ceil(overpayment)}')
            else:
                print(f'Incorrect parameters.')
        elif args.principal and args.payment and args.interest:
            if args.principal > 0 and args.payment > 0 and args.interest > 0:
                i = (args.interest / 12) / 100
                pl = args.principal
                pt = args.payment
                payment_cycles = math.ceil(math.log((pt/(pt-i*pl)), 1 + i))
                payment_cycles_year = round(payment_cycles // 12)
                payment_cycles_month = round(payment_cycles % 12)
                payment_cycles_year_ = ''
                payment_cycles_month_ = ''

                if payment_cycles_year == 0 or payment_cycles_month == 0:
                    if payment_cycles_year == 0:
                        if payment_cycles_month > 1:
                            print(f'It will take {payment_cycles_month} months to repay this loan!')
                        else:
                            print(f'It will take {payment_cycles_month} month to repay this loan!')
                    elif payment_cycles_month == 0:
                        if payment_cycles_year > 1:
                            print(f'It will take {payment_cycles_year} years to repay this loan!')
                        else:
                            print(f'It will take {payment_cycles_year} year to repay this loan!')
                elif payment_cycles_year > 1 and payment_cycles_month > 1:
                    activator = True
                    payment_cycles_year_ = f'{payment_cycles_year} years'
                    payment_cycles_month_ = f'{payment_cycles_month} months'
                elif payment_cycles_year > 1 and payment_cycles_month == 1:
                    activator = True
                    payment_cycles_year_ = f'{payment_cycles_year} years'
                    payment_cycles_month_ = f'{payment_cycles_month} month'
                elif payment_cycles_year == 1 and payment_cycles_month == 1:
                    activator = True
                    payment_cycles_year_ = f'{payment_cycles_year} year'
                    payment_cycles_month_ = f'{payment_cycles_month} month'
                elif payment_cycles_year == 1 and payment_cycles_month > 1:
                    activator = True
                    payment_cycles_year_ = f'{payment_cycles_year} year'
                    payment_cycles_month_ = f'{payment_cycles_month} months'

                if activator:
                    print('It will take {years} and {months} to repay this loan!'.format(years=payment_cycles_year_,
                                                                                         months=payment_cycles_month_))
                overpayment = (payment_cycles * pt) - pl
                print(f'Overpayment = {overpayment}')
            else:
                print(f'Incorrect parameters.')
        else:
            print(f'Incorrect parameters.')

else:
    print(f'Incorrect parameters.')


#ANNUITY PAYMENT
#first_divider = monthly_interest_rate * (1 + monthly_interest_rate) ** number_periods
#second_divider = ((1 + monthly_interest_rate) ** number_periods) - 1
#annuity_payment = loan_principal * (first_divider / second_divider)

##PRINCIPAL
#monthly_loan_interest = (float(input()) / 12) / 100
#first_divider = monthly_loan_interest * (1 + monthly_loan_interest) ** number_periods
#second_divider = ((1 + monthly_loan_interest) ** number_periods) - 1
#loan_principal = annuity_payment / (first_divider / second_divider)

##PAYMENT CYCLES
#payment_cycles = math.ceil(math.log((monthly_payment / (monthly_payment - monthly_interest_rate * loan_principal)), 1 + monthly_interest_rate))