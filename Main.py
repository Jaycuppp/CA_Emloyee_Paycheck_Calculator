hrs = float(input("Enter Hours:"))
rate = float(input("Enter PayRate:"))

# With Overtime Pay Calculation
if hrs > 40: 
    Overtime = hrs - 40
    Regulartime = 40 - Overtime 
    RegularPay = Regulartime * rate
    OvertimePay = Overtime * rate * 1.5
    ActualPay = RegularPay + OvertimePay

# No Overtime Pay Calculation
elif hrs <= 40:
    RegularPay = hrs * rate
    ActualPay = RegularPay
    
print(ActualPay)


def computepay(h, r):
    h = float(h)
    r = float(r)
    if h > 40:
        Overtime = h - 40
        RegularTime = h - Overtime
        OverTimePay = Overtime * r * 1.5
        RegularPay = RegularTime * r
        TotalPay = RegularPay + OverTimePay
        
    elif h <= 40:
        TotalPay = h * r
       
    return TotalPay

hrs = input("Enter Hours:")
r = input("Enter PayRate:")

p = computepay(hrs, r)
print("Pay", p)
