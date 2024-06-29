import tkinter as tk
from datetime import datetime, timedelta

def calculate_age_and_next_birthday():
    birth_date = entry_single.get()
    try:
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()

        # Calculate age
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += (today.replace(month=today.month-1 if today.month > 1 else 12, day=1) - timedelta(days=1)).day
        if months < 0:
            years -= 1
            months += 12

        # Calculate next birthday
        next_birthday = birth_date.replace(year=today.year)
        if today > next_birthday:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days

        result_label_single.config(text=f"Age: {years} years, {months} months, and {days} days\n"
                                        f"Days until next birthday: {days_until_birthday} days")
    except ValueError:
        result_label_single.config(text="Invalid date format. Please use YYYY-MM-DD.")

def calculate_age_difference():
    birth_date1 = entry1.get()
    birth_date2 = entry2.get()
    try:
        birth_date1 = datetime.strptime(birth_date1, '%Y-%m-%d')
        birth_date2 = datetime.strptime(birth_date2, '%Y-%m-%d')
        
        if birth_date1 > birth_date2:
            older_date = birth_date1
            younger_date = birth_date2
        else:
            older_date = birth_date2
            younger_date = birth_date1

        delta = older_date - younger_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        
        result_label_difference.config(text=f"Age difference: {years} years, {months} months, and {days} days")
    except ValueError:
        result_label_difference.config(text="Invalid date format. Please use YYYY-MM-DD.")

# Create the main window
root = tk.Tk()
root.title("Age and Birthday Calculator")

# Single Age and Next Birthday Calculator
tk.Label(root, text="Enter your birth date (YYYY-MM-DD):").pack(pady=10)
entry_single = tk.Entry(root)
entry_single.pack(pady=5)

calculate_button_single = tk.Button(root, text="Calculate Age and Next Birthday", command=calculate_age_and_next_birthday)
calculate_button_single.pack(pady=10)

result_label_single = tk.Label(root, text="Age and days until next birthday will be displayed here.")
result_label_single.pack(pady=20)

# Age Difference Calculator
tk.Label(root, text="Enter the first birth date (YYYY-MM-DD):").pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter the second birth date (YYYY-MM-DD):").pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

calculate_button_difference = tk.Button(root, text="Calculate Age Difference", command=calculate_age_difference)
calculate_button_difference.pack(pady=10)

result_label_difference = tk.Label(root, text="Age difference will be displayed here.")
result_label_difference.pack(pady=20)

# Run the application
root.mainloop()
