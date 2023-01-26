# Weekly Payrate
hrs = float(input("Enter Hours Worked In Past 7 Days:"))
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
    
print(f"Here is your paycheck amount for the past week {ActualPay}")


# Bi-Weekly Payrate
hrs = float(input("Enter Hours Worked In Past 14 Days:"))
rate = float(input("Enter PayRate:"))

# With Overtime Pay Calculation
if hrs > 80: 
    Overtime = hrs - 80
    Regulartime = 80 - Overtime 
    RegularPay = Regulartime * rate
    OvertimePay = Overtime * rate * 1.5
    ActualPay = RegularPay + OvertimePay

# No Overtime Pay Calculation
elif hrs <= 80:
    RegularPay = hrs * rate
    ActualPay = RegularPay
    
print(f"Here is your paycheck amount for the past week {ActualPay}")
