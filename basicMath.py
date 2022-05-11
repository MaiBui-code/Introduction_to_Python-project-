def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    a = [0,1]
    for i in range(2, n+1):
        a.append( (a[i-1] + a[i-2]))
    return a[n]

#print(last_digit_of_fibonacci_number(613455))

def lcm(a,b):
    best1 = []
    multi = a*b
    for m  in range (1, multi + 1):
        if (m % a == 0) and (m % b == 0):
            best1.append(m)
    return best1[0]

#print(lcm(33,63))

def last_digit_sum_fibo(n):
    a = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >1:
        sum1 = 1
        for i in range(2, n+1):
            a.append( a[i-1] + a[i-2])
            sum1 = sum1 + a[i]
        return sum1 % 10

#print(last_digit_sum_fibo(613455))

def gcd(a, b):

    if b == 0:
        return a
    elif b!= 0:
        return gcd(b, a % b)

#print(gcd(18,35))

