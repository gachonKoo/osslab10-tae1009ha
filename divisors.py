import sys

# 입력값을 받아서 정수로 변환
number = int(sys.argv[1])

# 약수를 저장할 리스트
divisors = []

# 1부터 number까지 반복
for i in range(1, number + 1):
    if number % i == 0:  # 나머지가 0이면 약수
        divisors.append(i)

# 결과를 공백으로 구분하여 출력
print(" ".join(map(str, divisors)))
