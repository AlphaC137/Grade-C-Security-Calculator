import tkinter as tk
from tkinter import messagebox

def calculate_salary(hours_worked, sundays_worked, holidays_worked, overtime_hours=0):
    hourly_rate = 27.53  # Rate per hour
    sunday_multiplier = 1.5  # Sunday pay multiplier (regular + half)
    holiday_multiplier = 2  # Holiday pay multiplier (double pay)
    
    # Regular pay calculation (for weekdays)
    regular_pay = hourly_rate * hours_worked
    
    # Pay for Sundays (extra half)
    sunday_pay = hourly_rate * sunday_multiplier * sundays_worked
    
    # Pay for Holidays (double pay)
    holiday_pay = hourly_rate * holiday_multiplier * holidays_worked
    
    # Overtime pay (same as regular pay)
    overtime_pay = hourly_rate * overtime_hours
    
    # Total monthly salary
    total_salary = regular_pay + sunday_pay + holiday_pay + overtime_pay
    
    return total_salary, regular_pay, sunday_pay, holiday_pay, overtime_pay

def display_salary_details():
    hours_per_day = float(entry_hours_per_day.get())
    working_days_per_month = int(entry_working_days.get())
    sundays_worked = int(entry_sundays.get())
    holidays_worked = int(entry_holidays.get())
    overtime_hours = int(entry_overtime.get())
    
    total_hours = hours_per_day * working_days_per_month

    # Calculate salary
    total_salary, regular_pay, sunday_pay, holiday_pay, overtime_pay = calculate_salary(
        total_hours, sundays_worked, holidays_worked, overtime_hours)
    
    result = (
        f"Regular Pay: R{regular_pay:.2f}\n"
        f"Sunday Pay (1.5x): R{sunday_pay:.2f}\n"
        f"Holiday Pay (2x): R{holiday_pay:.2f}\n"
        f"Overtime Pay: R{overtime_pay:.2f}\n"
        f"Total Monthly Salary: R{total_salary:.2f}"
    )
    messagebox.showinfo("Salary Breakdown", result)

# Create the main window
root = tk.Tk()
root.title("Salary Calculator")

# Create and place the input fields and labels
tk.Label(root, text="Hours worked per day:").grid(row=0, column=0, padx=10, pady=5)
entry_hours_per_day = tk.Entry(root)
entry_hours_per_day.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Working days per month:").grid(row=1, column=0, padx=10, pady=5)
entry_working_days = tk.Entry(root)
entry_working_days.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Sundays worked:").grid(row=2, column=0, padx=10, pady=5)
entry_sundays = tk.Entry(root)
entry_sundays.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Holidays worked:").grid(row=3, column=0, padx=10, pady=5)
entry_holidays = tk.Entry(root)
entry_holidays.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Overtime hours:").grid(row=4, column=0, padx=10, pady=5)
entry_overtime = tk.Entry(root)
entry_overtime.grid(row=4, column=1, padx=10, pady=5)

# Create and place the calculate button
tk.Button(root, text="Calculate Salary", command=display_salary_details).grid(row=5, column=0, columnspan=2, pady=20)

# Run the GUI event loop
root.mainloop()
