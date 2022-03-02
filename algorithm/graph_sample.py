import sys; sys. stdin = open('graph_input.txt')

# 인접 행렬
# V, E = map(int, input().split()) # 정점수, 간선수
# # 0번인덱스를 건너뛰고 1번인덱스부터.
# # 만약 0번 정점이 있으면 0번인덱스부터 세어주기.
# G = [[0] * (V + 1) for _ in range(V+1)]
#
# # 간선수 만큼 입력
# for _ in range(E):
#     u, v = map(int, input().split())
#     G[u][v] = 1
#     G[v][u] = 1
# # 정점이 1번부터 있으므로 index 1부터 그냥 표현하도록 슬라이싱
# for lst in G[1:]:
#     print(*lst[1:])

# # 인접 리스트
# V, E = map(int, input().split()) # 정점수, 간선수
# # 0번인덱스를 건너뛰고 1번인덱스부터.
# # 내가 찾고싶은 시작정점이 index가 되고 그 index가 가리키는 리스트의 인자가 도착정점이 된다.
# # 만약 0번 정점이 있으면 0번인덱스부터 세어주기.
# G = [[] for _ in range(V+1)]
#
# # 간선수 만큼 입력
# for _ in range(E):
#     u, v = map(int, input().split())
#     # 무방향이므로 양쪽을 다 입력해준다.
#     # 유방향이면 한쪽만 입력.
#     G[u].append(v)
#     G[v].append(u)
#
# for i in range(1, V + 1):
#     print(i, '-->', G[i])

# DFS 재귀

V, E = map(int, input().split()) # 정점수, 간선수
# 0번인덱스를 건너뛰고 1번인덱스부터.
# 내가 찾고싶은 시작정점이 index가 되고 그 index가 가리키는 리스트의 인자가 도착정점이 된다.
# 만약 0번 정점이 있으면 0번인덱스부터 세어주기.
G = [[] for _ in range(V+1)]

# 간선수 만큼 입력
for _ in range(E):
    u, v = map(int, input().split())
    # 무방향이므로 양쪽을 다 입력해준다.
    # 유방향이면 한쪽만 입력.
    G[u].append(v)
    G[v].append(u)
# DFS에 필요한것: Graph, stack, 방문정보(visit)
# 방문정보가 없으면 무한루프에 빠질 수 있다. 한번 간 곳은 가지 말라고 체크.
# 그래프의 정점의 수 만큼 방문정보가 필요하다.
visited = [0] * (V + 1) # 정점 수 만큼 방문정보 저장하는 배열 (0번은 안쓰고 1~V까지)
# DFS 재귀 # 재귀에서는 stack이 시스템적으로 기록되기 때문에 필요없다.
def DFS(v): # 현재 방문하는 정점 번호를 매개변수로 반드시 포함.
    # 방문 표시 하고
    visited[v] = 1
    # v의 인접 정점을 찾는다.
    for w in G[v]:
        # 방문정보를 체크하고 없으면 go
        if not visited[w]: # w에 0이라고 적혀있으면
            DFS(w)

DFS(1)#시작 정점이 1번이라면