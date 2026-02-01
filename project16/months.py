import calendar
from datetime import datetime

# 1. Get the current month from the system
current_date = datetime.now()
current_month_num = current_date.month

# 2. Convert month number to name using the calendar module
current_month_name = calendar.month_name[current_month_num]

# 3. Get month details using strftime (string format time)
abbreviated_name = current_date.strftime("%b")

# 4. Get the number of days in the current month
# calendar.monthrange returns (first_day_of_week, total_days)
_, total_days = calendar.monthrange(current_date.year, current_month_num)

# --- DISPLAY RESULTS ---

print(f"--- Month Report ---")
print(f"Numerical Month:  {current_month_num}")
print(f"Full Month Name:  {current_month_name}")
print(f"Abbreviation:     {abbreviated_name}")
print(f"Days in Month:    {total_days}")

print("\n--- List of All Months ---")
# Skipping index 0 because it's an empty string in calendar.month_name
for i in range(1, 13):
    print(f"{i}: {calendar.month_name[i]}")