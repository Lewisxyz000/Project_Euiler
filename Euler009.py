import math

n = 1
m = 2



while True:
    result = math.pow(m, 2) + m * n  #계산 수행

    if result == 500:
        print(m, n)
        break

    m += 1  #값을 증가시키며 결과를 구한다
    if m == 500:
        n += 1
        m = n + 1  #m이 상한값을 넘어버릴 경우에 n을 중가시키고 m을 n + 1로 만든다

a = math.pow(m, 2) - math.pow(n, 2)
b = 2 * m * n
c = math.pow(m, 2) + math.pow(n, 2)

print(a, b, c)
print(a + b + c)
print(a * b * c)