
def func(P: int, R : int, L : int) -> int:
    R_to_monthly_percent = R / (12 * 100)
    
    return (R_to_monthly_percent * P) / (1 - pow((1 + R_to_monthly_percent), -L))
    
#P = r(V)/ 1 - (1+r)^-n
#new
if __name__ == '__main__':
    print(50+50)
    print(100 - 10)
    print("Hello World: 10")
    print("answer = ", func(800000,6,103))