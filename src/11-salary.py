salary = float(input("Enter Employee Salary: "))

hra_da_pf_total = (10 + 5 + 3)
exp_of_hdp = (salary / 100) * hra_da_pf_total


def calc_tax_on_salary(salary):
    if salary <= 100000:
        return 0
    elif salary <= 1000000:
        return (salary / 100) * 10
    elif salary <= 2000000:
        return (salary / 100) * 20
    else:
        return (salary / 100) * 30


in_hand_salary = salary - exp_of_hdp - calc_tax_on_salary(salary)

print(f"In hand salary: {in_hand_salary}")
