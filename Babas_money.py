"""

p = principle (present value)
r = interest rate
n = how many payments per period
t = how many periods

"""

def compound_intrest():
    p = float(input("What's the principle "))
    r = float(input("What's the rate "))
    n = int(input("How many periods per year"))
    t = int(input('How many years '))
    pv = p * (pow((1 + r/100/n),n*t))

    balance = p * (pow((1+ r/100/n), n*t))
    ci = balance - p
    print ('\nYour balance at the end of the period will be $',round(balance, 2))
    print('\nYou earned $',round(ci,2), 'during the',t,'year period.')
    roi = ci/balance*100
    print("This is a ",round(roi,2),'% return on investment')

compound_intrest()
