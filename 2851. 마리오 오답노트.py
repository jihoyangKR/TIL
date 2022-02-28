# 틀린 코드.
# while문 안에서 i가 다 돌고 다시 for 문의 i가 도는걸 생각해야하는데 그걸 간과했음
# 반례 1 1 1 1 1 1 1 1 1 1
over_100 = 0
data = []
for i in range(10):
    data.append(int(input()))
for i in range(10):
    while over_100 <= 100:
        over_100 += data[i]
        under_100 = over_100 - data[i]
        i += 1
        if i == 10:
            break
if 100 - under_100 < over_100 - 100:
    print(under_100)
else:
    print(over_100)

# 맞은 코드
# if sum_num - 100 <= (100 - (sum_num - data[i])): 문에서
# (100 - (sum_num - data[i])) (sum_num - data[i])를 먼재 해줘야한다. 사실 무슨차이인지는 잘 모르겠음
data = [int(input()) for _ in range(10)]
num = []
sum_num = 0
for i in range(10):
    sum_num += data[i]
    if sum_num > 100:
        if sum_num - 100 <= (100 - (sum_num - data[i])):
            print(sum_num)
        else:
            print(sum_num-data[i])
        break
else:
    print(sum_num)