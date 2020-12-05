"""

p = principle (present value)
r = interest rate
n = how many payments per period
t = how many periods

"""

p = float(input("What's the principle "))
r = float(input("What's the rate "))
n = int(input("How many periods "))
t = int(input("How many payments per period "))
pv = p * (pow((1 + r/100/n),n*t))

print (pv)

def compund_intrest(p, r, n, t):
    balance = p * (oiw((1+ r/100/n), n*t))
    ci = balance - p
    print ('Balance at the end of the period ', round(balance, 2))
    print("Intrest earned is ", round(ci,2))

compund_intrest(5000,10,12,5)
