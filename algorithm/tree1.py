'''
4
1 2 1 3 3 4 3 5
'''

# def pre(v):
#     if v: # 0번 정점이 없으므로.. 0번은 자식이 없는 경우를 표시
#         print(v) # visit(v)에 해당
#         pre(c1[v])
#         pre(c2[v])
#
# def in_order(v):
#     if v:
#         in_order(c1[v])
#         print(v)
#         in_order(c2[v])
#
# def post_order(v):
#     if v:
#         post_order(c1[v])
#         post_order(c2[v])
#         print(v)
#
#
# E = int(input()) # 간선 수
# arr = list(map(int, input().split()))
# V = E + 1 # 정점 수 (간선 보다 정점이 하나 더 많다), 1번부터 V번까지 정점이 있을 때 마지막 정점과 일치
#
# # 부모 번호를 인덱스로 자식번호 저장
# c1 = [0] * (V + 1)
# c2 = [0] * (V + 1)
# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
#     if c1[p] == 0:
#         c1[p] = c
#     else:
#         c2[p] = c
# # print(c1)
# # print(c2)
#
# pre(1)
# in_order(1)
# post_order(1)

#
# for tc in range(1, 11):
#     N = int(input())
#     V = [0] * (N + 1)
#     for i in range(N):
#         data = input().split()
#     print(data)

def in_order(v):
    if v <= N:
        in_order(v * 2)
        print(V[v], end=' ')
        in_order(v*2 + 1)

for tc in range(1, 11):
    N = int(input())
    V = [0] * (N + 1)
    for i in range(N):
        data = input().split()
        V[int(data[0])] = data[1]
    print(f'#{tc}', end=' ')
    in_order(1)
    print()







# # 자식 번호를 인덱스로 부모 번호를 저장
# par = [0]*(V + 1)
# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
#     par[c] = p
#
#
# # root 찾기
# root = 0
# for i in range(1, V + 1):
#     if par[i] == 0:
#         root = i
#         break
# print(root)




