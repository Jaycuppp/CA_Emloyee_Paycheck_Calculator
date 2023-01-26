class Employee_Payrate():
    def WeeklyPayTrack(OvertimeHours = 40):
        # Weekly Payrate
        hrs = float(input("Enter Hours Worked In Past 7 Days: "))
        rate = float(input("Enter PayRate: "))

        # With Overtime Pay Calculation
        if hrs > OvertimeHours: 
            Overtime = hrs - OvertimeHours
            Regulartime = hrs - Overtime 
            RegularPay = Regulartime * rate
            OvertimePay = Overtime * rate * 1.5
            ActualPay = RegularPay + OvertimePay

        # No Overtime Pay Calculation
        elif hrs <= OvertimeHours:
            RegularPay = hrs * rate
            ActualPay = RegularPay

        print(f"Here is your paycheck amount for the past week {ActualPay}")
    
    def BiWeeklyPayTrack(OvertimeHours = 80):
        # BiWeekly Payrate
        hrs = float(input("Enter Hours Worked In Past 14 Days: "))
        rate = float(input("Enter PayRate: "))

        # With Overtime Pay Calculation
        if hrs > OvertimeHours: 
            Overtime = hrs - OvertimeHours
            Regulartime = hrs - Overtime 
            RegularPay = Regulartime * rate
            OvertimePay = Overtime * rate * 1.5
            ActualPay = RegularPay + OvertimePay

        # No Overtime Pay Calculation
        elif hrs <= OvertimeHours:
            RegularPay = hrs * rate
            ActualPay = RegularPay

        print(f"Here is your paycheck amount for the past week {ActualPay}")

Employee_Payrate.WeeklyPayTrack()
Employee_Payrate.BiWeeklyPayTrack()
