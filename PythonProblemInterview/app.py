def reverse(s):
    temp = ""
    for ch in s:
        temp = ch + temp
    return temp


s = "Python is fun"
print(reverse(s))


def max_salary_employee(employees):
    max = 0
    emp1 = None
    for emp in employees:
        if max < emp.get('salary'):
            max = emp.get('salary')
            emp1 = emp
    return emp1


employees = [
    {"name": "John", "salary": 3000, "designation": "developer"},
    {"name": "Emma", "salary": 4000, "designation": "manager"},
    {"name": "Kelly", "salary": 3500, "designation": "tester"}]

print(max_salary_employee(employees))
