from tkinter import *

def Run():
    root = Tk()
    root.title("HR Helper Tool")

    # Frame for Root Widget
    frame = LabelFrame(root, padx=20, pady=20)
    frame.pack(padx=5, pady=5)

    
    # Function for calling the correct version of the Payroll Logic
    def Payroll_Window(Parameter):
        if Parameter == 'Weekly':
            def Weekly_Payroll_Calculation():
                # User Input and Constant Vars
                User_Hours = float(Hour_Entry.get())
                User_Wage = float(Wage_Entry.get())
                FullTime = 40
                Overtime_Multi = 1.5

                # California Tax Rate Thresholds based on Hourly Wages in USD $
                Tax_Threshold_One = 5.72916667
                Tax_Threshold_Two = 23.2942708
                Tax_Threshold_Three = 49.6744792
                Tax_Threshold_Four = 94.84375
                Tax_Threshold_Five = 120.442708
                Tax_Threshold_Six = 310.106771
                
                # California Income Tax Bracket %s So Far for the Year of 2023
                Tax_Bracket_One = 0.10
                Tax_Bracket_Two = 0.12
                Tax_Bracket_Three = 0.22
                Tax_Bracket_Four = 0.24
                Tax_Bracket_Five = 0.32
                Tax_Bracket_Six = 0.35
                Tax_Bracket_Seven = 0.37
                        
                # With Overtime Pay Calculation
                if User_Hours > FullTime: 
                    Overtime = User_Hours - FullTime
                    Regulartime = User_Hours - Overtime 
                    RegularPay = Regulartime * User_Wage
                    OvertimePay = Overtime * User_Wage * Overtime_Multi
                    ActualPay = RegularPay + OvertimePay

                # No Overtime Pay Calculation
                elif User_Hours <= FullTime:
                    ActualPay = User_Hours * User_Wage

                if 0 < User_Wage <= Tax_Threshold_One:
                    Income_Tax_Percentage = Tax_Bracket_One

                elif Tax_Threshold_One < User_Wage <= Tax_Threshold_Two :
                    Income_Tax_Percentage = Tax_Bracket_Two

                elif Tax_Threshold_Two < User_Wage <= Tax_Threshold_Three:
                    Income_Tax_Percentage = Tax_Bracket_Three
                    
                elif Tax_Threshold_Three < User_Wage <= Tax_Threshold_Four:
                    Income_Tax_Percentage = Tax_Bracket_Four
                    
                elif Tax_Threshold_Four < User_Wage <= Tax_Threshold_Five:
                    Income_Tax_Percentage = Tax_Bracket_Five
                    
                elif Tax_Threshold_Five < User_Wage <= Tax_Threshold_Six:
                    Income_Tax_Percentage = Tax_Bracket_Six
                    
                elif Tax_Threshold_Six < User_Wage:
                    Income_Tax_Percentage = Tax_Bracket_Seven

                # Now Factoring In the Tax Rate
                Amount_Taxed = ActualPay * Income_Tax_Percentage
                Post_Tax_Pay = ActualPay - Amount_Taxed

                Rounded_Pre_Tax_Pay = round(ActualPay, 2)
                Rounded_Amount_Taxed = round(Amount_Taxed, 2)
                Rounded_Post_Tax_Pay = round(Post_Tax_Pay, 2)

                # Displaying the Post Calculation Results
                Pre_Tax_Income_Label = Label(Top, text=f"Total Pre Tax Payment: ${Rounded_Pre_Tax_Pay}")
                Pre_Tax_Income_Label.grid(row=3, column=0, columnspan=3, pady=4)

                Income_Getting_Taxed_Label = Label(Top, text=f"Total Being Taxed: ${Rounded_Amount_Taxed}")
                Income_Getting_Taxed_Label.grid(row=4, column=0, columnspan=3, pady=4)

                Post_Tax_Income_Label = Label(Top, text=f"Total Post Tax Payment: ${Rounded_Post_Tax_Pay}")
                Post_Tax_Income_Label.grid(row=5, column=0, columnspan=3, pady=4)

                def ClearAll():
                    Pre_Tax_Income_Label.after(0, Pre_Tax_Income_Label.destroy())
                    Income_Getting_Taxed_Label.after(0, Income_Getting_Taxed_Label.destroy())
                    Post_Tax_Income_Label.after(0, Post_Tax_Income_Label.destroy())
                    Clear_Button.after(0, Clear_Button.destroy())
                    
                Clear_Button = Button(Top, text="Clear Above Results", command=ClearAll)
                Clear_Button.grid(row=6, column=0, columnspan=3, pady=4)

            
            # Setup for the 2nd Window
            Top = Toplevel()
            Top.title('Weekly Payroll')
            Top.geometry("300x200")
            
            # Hours Worked Lable,Input, and Button
            Hour_Label = Label(Top, text="Hours Worked:")
            Hour_Label.grid(row=0, column=0)

            Hour_Entry = Entry(Top, width=10)
            Hour_Entry.grid(row=0, column=1)
            Hour_Entry.insert(0, 'Enter Here')

            # Input Box and Label for Hourly Wage
            Wage_Label = Label(Top, text="Hourly Wage:")
            Wage_Label.grid(row=1, column=0)

            Wage_Entry = Entry(Top, width=10)
            Wage_Entry.grid(row=1, column=1)
            Wage_Entry.insert(0, 'Enter Here')

            # Result Button After Inputs Have Been Made
            Results_Button = Button(Top, text="Calculate Payroll", command=Weekly_Payroll_Calculation)
            Results_Button.grid(row=2, column=0, columnspan=2, pady=2)


        if Parameter == 'Bi-Weekly':
            def Bi_Weekly_Payroll_Calculation():
                # User Input and Constant Vars
                User_Hours = float(Hour_Entry.get())
                User_Wage = float(Wage_Entry.get())
                FullTime = 80
                Overtime_Multi = 1.5

                # California Tax Rate Thresholds based on Hourly Wages in USD $
                Tax_Threshold_One = 5.72916667
                Tax_Threshold_Two = 23.2942708
                Tax_Threshold_Three = 49.6744792
                Tax_Threshold_Four = 94.84375
                Tax_Threshold_Five = 120.442708
                Tax_Threshold_Six = 310.106771
                
                # California Income Tax Bracket %s So Far for the Year of 2023
                Tax_Bracket_One = 0.10
                Tax_Bracket_Two = 0.12
                Tax_Bracket_Three = 0.22
                Tax_Bracket_Four = 0.24
                Tax_Bracket_Five = 0.32
                Tax_Bracket_Six = 0.35
                Tax_Bracket_Seven = 0.37
                        
                # With Overtime Pay Calculation
                if User_Hours > FullTime: 
                    Overtime = User_Hours - FullTime
                    Regulartime = User_Hours - Overtime 
                    RegularPay = Regulartime * User_Wage
                    OvertimePay = Overtime * User_Wage * Overtime_Multi
                    ActualPay = RegularPay + OvertimePay

                # No Overtime Pay Calculation
                elif User_Hours <= FullTime:
                    ActualPay = User_Hours * User_Wage

                if 0 < User_Wage <= Tax_Threshold_One:
                    Income_Tax_Percentage = Tax_Bracket_One

                elif Tax_Threshold_One < User_Wage <= Tax_Threshold_Two :
                    Income_Tax_Percentage = Tax_Bracket_Two

                elif Tax_Threshold_Two < User_Wage <= Tax_Threshold_Three:
                    Income_Tax_Percentage = Tax_Bracket_Three
                    
                elif Tax_Threshold_Three < User_Wage <= Tax_Threshold_Four:
                    Income_Tax_Percentage = Tax_Bracket_Four
                    
                elif Tax_Threshold_Four < User_Wage <= Tax_Threshold_Five:
                    Income_Tax_Percentage = Tax_Bracket_Five
                    
                elif Tax_Threshold_Five < User_Wage <= Tax_Threshold_Six:
                    Income_Tax_Percentage = Tax_Bracket_Six
                    
                elif Tax_Threshold_Six < User_Wage:
                    Income_Tax_Percentage = Tax_Bracket_Seven

                # Now Factoring In the Tax Rate
                Amount_Taxed = ActualPay * Income_Tax_Percentage
                Post_Tax_Pay = ActualPay - Amount_Taxed

                Rounded_Pre_Tax_Pay = round(ActualPay, 2)
                Rounded_Amount_Taxed = round(Amount_Taxed, 2)
                Rounded_Post_Tax_Pay = round(Post_Tax_Pay, 2)

                Pre_Tax_Income_Label = Label(Top, text=f"Total Pre-Tax Payment: {Rounded_Pre_Tax_Pay}")
                Pre_Tax_Income_Label.grid(row=3, column=0, columnspan=2, pady=4)

                Income_Getting_Taxed_Label = Label(Top, text=f"Total Being Taxed: {Rounded_Amount_Taxed}")
                Income_Getting_Taxed_Label.grid(row=4, column=0, pady=4)

                Post_Tax_Income_Label = Label(Top, text=f"Total Post-Tax Payment: {Rounded_Post_Tax_Pay}")
                Post_Tax_Income_Label.grid(row=5, column=0, pady=4)

                def ClearAll():
                    Pre_Tax_Income_Label.after(0, Pre_Tax_Income_Label.destroy())
                    Income_Getting_Taxed_Label.after(0, Income_Getting_Taxed_Label.destroy())
                    Post_Tax_Income_Label.after(0, Post_Tax_Income_Label.destroy())
                    Clear_Button.after(0, Clear_Button.destroy())
                    
                Clear_Button = Button(Top, text="Clear Above Results", command=ClearAll)
                Clear_Button.grid(row=6, column=0, columnspan=3, pady=4)

            # Setup for the 2nd Window
            Top = Toplevel()
            Top.title('Bi-Weekly Payroll')
            Top.geometry("300x200")

            # Input Box and Label for Hours Worked
            Hour_Label = Label(Top, text="Hours Worked:")
            Hour_Label.grid(row=0, column=0)

            Hour_Entry = Entry(Top, width=10)
            Hour_Entry.grid(row=0, column=1)
            Hour_Entry.insert(0, "Enter Here")

            # Input Box and Label for Hourly Wage
            Wage_Label = Label(Top, text="Hourly Wage:")
            Wage_Label.grid(row=1, column=0)

            Wage_Entry = Entry(Top, width=10)
            Wage_Entry.grid(row=1, column=1)
            Wage_Entry.insert(0, "Enter Here")

            # Result Button After Inputs Have Been Made
            Results_Button = Button(Top, text="Calculate Payroll", command= Bi_Weekly_Payroll_Calculation)
            Results_Button.grid(row=2, column=0, columnspan=2, pady=4)

    # Weekly Payroll Widget Setup
    Weekly_Payroll = Button(frame, padx=20, pady=10, fg="Black", bg="Red", text="Weekly Payroll", command= lambda: Payroll_Window('Weekly'))
    Weekly_Payroll.grid(row=0, column=0, padx=70, pady=20)
    
    # Bi-Weekly Payrool Widget Setup
    Bi_Weekly_Payroll = Button(frame, padx=20,  pady=10, fg="Black", bg="Red", text="Bi-Weekly Payroll", command= lambda: Payroll_Window('Bi-Weekly'))
    Bi_Weekly_Payroll.grid(row=1, column=0, padx=70, pady=20)

    root.mainloop()