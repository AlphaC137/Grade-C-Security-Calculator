# salary_calculator.py
# A script to calculate monthly salary based on hours worked, Sunday work, holiday work, and overtime.

def calculate_salary(hours_worked, sundays_worked, holidays_worked, overtime_hours=0):
    """
    Calculate the monthly salary considering:
    - Regular hours worked
    - Sunday pay (1.5x rate)
    - Holiday pay (2x rate)
    - Overtime pay (same as regular rate)

    :param hours_worked: Total hours worked in a month (excluding weekends and holidays)
    :param sundays_worked: Number of Sundays worked
    :param holidays_worked: Number of holidays worked
    :param overtime_hours: Number of overtime hours worked (optional, defaults to 0)
    
    :return: Total salary, and detailed breakdown of payments
    """
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

def display_salary_details(hours_per_day, working_days_per_month, sundays_worked, holidays_worked, overtime_hours=0):
    """
    Display the salary breakdown including regular pay, Sunday pay, holiday pay, and overtime pay.
    
    :param hours_per_day: Number of hours worked per day
    :param working_days_per_month: Number of working days in a month
    :param sundays_worked: Number of Sundays worked
    :param holidays_worked: Number of holidays worked
    :param overtime_hours: Number of overtime hours worked (optional)
    """
    total_hours = hours_per_day * working_days_per_month

    # Calculate salary
    total_salary, regular_pay, sunday_pay, holiday_pay, overtime_pay = calculate_salary(
        total_hours, sundays_worked, holidays_worked, overtime_hours)
    
    print("\n---- Salary Breakdown ----")
    print(f"Regular Pay: R{regular_pay:.2f}")
    print(f"Sunday Pay (1.5x): R{sunday_pay:.2f}")
    print(f"Holiday Pay (2x): R{holiday_pay:.2f}")
    print(f"Overtime Pay: R{overtime_pay:.2f}")
    print(f"Total Monthly Salary: R{total_salary:.2f}")

# If you want to run this script, use the code below to prompt the user for input.

if __name__ == "__main__":
    # Input: User details
    hours_per_day = float(input("Enter the number of hours worked per day: "))
    working_days_per_month = int(input("Enter the number of working days in a month (excluding Sundays and holidays): "))
    sundays_worked = int(input("Enter the number of Sundays worked: "))
    holidays_worked = int(input("Enter the number of holidays worked: "))
    overtime_hours = int(input("Enter the number of overtime hours worked: "))

    # Display the salary breakdown
    display_salary_details(hours_per_day, working_days_per_month, sundays_worked, holidays_worked, overtime_hours)
