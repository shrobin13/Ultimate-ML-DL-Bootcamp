principal = float("Enter the principal amount: ")
rate = float("Enter the rate of interest (% per year): ")
time = float("Enter the time period (in years): ")

simple_interest = (principal * rate * time) / 100

print(f"\nSimple Interest: {simple_interest:.2f}")
