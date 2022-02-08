import math

def monthly_payment(P: int, R : int, L : int) -> int:
    R_to_monthly_percent = R / (12 * 100)
    
    return math.ceil((R_to_monthly_percent * P) / (1 - pow((1 + R_to_monthly_percent), -L)))
    
if __name__ == '__main__':
    print(50+50)
    print(100 - 10)
    print(pow(6,6))
    print(6+6+6+6+6+6)
    print("Hello World: 10")
    print("answer = ", monthly_payment(800000,6,103))