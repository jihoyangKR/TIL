V, E = map(int, input().split())
tree = [[0] * 3 for _ in range(V + 1)]
# 왼쪽, 오른쪽, 부모를 표현하는 1차원 배열을 명시적으로 만들어준다.
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))

# 2개씩 끊어 E번 반복해서 읽기
# 2개씩 묶은게 E개 이므로 E * 2가 전체 목록
for i in range(E * 2, 2):
    p, c = arr[i], arr[i + 1] # p가 부모, c가 자식
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p # c의 부모는 p이다.


def inorder(v):
    if v == 0: return

    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])

inorder(1)