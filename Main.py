Weekly_Hours = 40
Bi_Weekly_Hours = 80
Over_Time_Multiplier = 1.5

class HRTool():
    def TotalPay(Weekly_Hours, Over_Time_Multiplier, Days_Worked):
        # Weekly Payrate
        hrs = float(input(f"Enter Hours Worked In Past {Days_Worked} Days: "))
        rate = float(input("Enter PayRate: "))

        # With Overtime Pay Calculation
        if hrs > Weekly_Hours: 
            Overtime = hrs - Weekly_Hours
            Regulartime = hrs - Overtime 
            RegularPay = Regulartime * rate
            OvertimePay = Overtime * rate * Over_Time_Multiplier
            ActualPay = RegularPay + OvertimePay

        # No Overtime Pay Calculation
        elif hrs <= Weekly_Hours:
            RegularPay = hrs * rate
            ActualPay = RegularPay

        print(f"Here is your paycheck amount for the past {Days_Worked} days: ${ActualPay}")
        return 0

if __name__ == "__main__":
    Weekly_Pay_Amount = HRTool.TotalPay(Weekly_Hours, Over_Time_Multiplier, 7)
    Bi_Weekly_Pay_Amount = HRTool.TotalPay(Bi_Weekly_Hours, Over_Time_Multiplier, 14)
