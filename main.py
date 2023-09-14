import decimal


def calculate_pi(iterations):
    decimal.getcontext().prec = 120
    pi = decimal.Decimal(0)
    sign = 1
    for i in range(iterations):
        term = decimal.Decimal(1) / decimal.Decimal(2 * i + 1)
        pi += sign * term
        sign *= -1
    return 4 * pi


iterations = int(input("Enter count of iterations "))
result = calculate_pi(iterations)
print(f" π after {iterations} iterations :\n{result}")
