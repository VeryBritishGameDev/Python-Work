
def zero_one(num):
    if num == 1:
        num = 0
    else:
        num = 1
    return(num)

def zero_one_b(num):
    num = not num
    return int(num)

def counter_zero_one(num):
    return (num % 2)

x=1

for i in range(1,21):
    x = zero_one_b(x)
    y = counter_zero_one(x)
    print(f"y , counter {y}, {i}")           
