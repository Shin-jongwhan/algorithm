# 최대공약수 GCD (greatest common divisor)
### 간단하긴 한데 나중에 까먹을까봐 정리하였다.
### 유클리드 호제법(Euclidean Algorithm)을 사용하면 간단하다.
### a, b의 나머지를 계속 구하면서, b의 나머지가 0이 될 때까지 반복한다.
### 나머지 연산은 a % b에서 a < b일 경우 a의 값이 그대로 출력된다.
```
def gcd(a, b):
    while b != 0:
        # a, b = (초기값 18, 26 -> )26, 18 -> 18, 8 -> 8, 2 -> 2, 0
        a, b = b, a % b
    return a

a = 18
b = 26
g = gcd(a, b)  # 결과: 2

# 결과 구하기
reduced_a = a // g  # 18 // 2 = 9
reduced_b = b // g  # 26 // 2 = 13
```
### <br/><br/><br/>


# 최소공배수 LCM (least common multiple)
### GCD를 활용해서 풀 수 있다.
### // 을 써서 gcd로 나눈 정수값을 얻는다.
```
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

result = lcm(a, b)
```

