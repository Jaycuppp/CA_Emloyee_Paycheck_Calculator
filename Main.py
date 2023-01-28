class WeeklyPayRate():
    def TotalPay(Over_Time_Hours = 40, Over_Time_Multiplier = 1.5):
        # Weekly Payrate
        hrs = float(input("Enter Hours Worked In Past 7 Days: "))
        rate = float(input("Enter PayRate: "))

        # With Overtime Pay Calculation
        if hrs > Over_Time_Hours: 
            Overtime = hrs - Over_Time_Hours
            Regulartime = hrs - Overtime 
            RegularPay = Regulartime * rate
            OvertimePay = Overtime * rate * Over_Time_Multiplier
            ActualPay = RegularPay + OvertimePay

        # No Overtime Pay Calculation
        elif hrs <= Over_Time_Hours:
            RegularPay = hrs * rate
            ActualPay = RegularPay

        print(f"Here is your paycheck amount for the past week {ActualPay}")
        return 0

class BiWeeklyPayRate(WeeklyPayRate):
    pass

WeeklyPayRate.TotalPay()
BiWeeklyPayRate.TotalPay(80, 1.5)
