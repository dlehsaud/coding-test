# 자료형
a = 1e9
print(a)

a = 3954e-3
print(a)

a = 0.3 + 0.6
print(round(a, 4))

a = 7
b = 3

print(a/b)
print(a//b)
print(a%b)
print(a**b)

# 리스트 자료형
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[4])

# 빈 리스트(1)
a = list()
print(a)
# 빈 리스트(2)
a = []
print(a)

# 모든 값 0으로 초기화
n = 10
a = [0] * n
print(a)

# 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])

print(a[-3])

a[3] = 7
print(a)

# 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])

# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

# 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 언더바(_)
for _ in range(5):
  print('Hello World')

# 메서드
a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입(끝) - O(1)
a.append(2)
print("삽입: ", a)

# 오름차순 정렬 - O(NlogN)
a.sort()
print("오른차순 정렬: ", a)

# 내림차순 정렬 - O(NlogN)
a.sort(reverse=True)
print("내림차순 정렬 ", a)

# 리스트 원소 뒤집기 - O(N)
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가 - O(N)
a.insert(2, 3)
print("인덱스 2에 3추가: ", a)

# 특정 값인 데이터 개수 세기 - O(N)
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제 - O(N)
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만 저장
result = [i for i in a if i not in remove_set]
print(result)

data = 'Hello World'
print(data)

data = "Don't you know \"python\"?"ㅔㅕ