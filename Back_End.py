class HRTools():
    def TotalPay(Standard_Work_Hours, Over_Time_Multiplier, Days_Worked):
        # Vars Needed for Payrate Calc to work
        Total_Hours_Worked = float(input(f"Enter Hours Worked In Past {Days_Worked} Days: "))
        Pay_Rate = float(input("Enter PayRate: "))

        # With Overtime Pay Calculation
        if Total_Hours_Worked > Standard_Work_Hours: 
            Overtime = Total_Hours_Worked - Standard_Work_Hours
            Regulartime = Total_Hours_Worked - Overtime 
            RegularPay = Regulartime * Pay_Rate
            OvertimePay = Overtime * Pay_Rate * Over_Time_Multiplier
            ActualPay = RegularPay + OvertimePay

        # No Overtime Pay Calculation
        elif Total_Hours_Worked <= Standard_Work_Hours:
            RegularPay = Total_Hours_Worked * Pay_Rate
            ActualPay = RegularPay

        return print(f"Here is your paycheck amount for the past {Days_Worked} days: ${ActualPay}")


if __name__ == "__main__":
    # Important Vars
    Weekly_Hours = 40
    Bi_Weekly_Hours = 80
    Over_Time_Multiplier = 1.5

    Employee_Choice = str(input("Hello, Enter one of the following\n1) Paycheck Amount for past 1 Week of Work \n2) Paycheck Amount for past 2 Weeks of Work\n"))

    while Employee_Choice != "1" and Employee_Choice != "2":
        Employee_Choice = input("Sorry Invalid Choice. Please enter the numerical value for one of these choicses\n1) Paycheck Amount for past 1 Week of Work\n2)Paycheck Amount for past 2 Weeks of Work\n")

    if Employee_Choice == '1':
        Weekly_Pay_Amount = HRTools.TotalPay(Weekly_Hours, Over_Time_Multiplier, 7)
    if Employee_Choice == '2':
            Bi_Weekly_Pay_Amount = HRTools.TotalPay(Bi_Weekly_Hours, Over_Time_Multiplier, 14)
