# BFS

- DFS와 똑같이 시작점에서 경로가 존재하는 모든 정점들을 방문한다.
  - 경로 유무를 묻는 문제 ==> DFS, BFS로 다 가능
  - 결합 컴포넌트를 찾는 문제에서 많이 사용된다. 
    - connected component
  - 최단경로를 찾는 문제 => BFS로 해결한다.
    - DFS가 안되는건 아니나 DFS로 풀려면 원 알고리즘을 수정해야 한다.
    - DFS는 인접정점중 인접정점중 하나를 선택해 깊게 들어가는 형식이기 때문이다.
    - 그 때문에 운에 따라 최단경로를 갈지 안갈지 알 수 없다.

- DFS와의 차이점
  - DFS는 출발점에서 경로가 있는 임의 정점을 처음 방문할 때 최단으로 방문한다는 보장을 못한다.
  - BFS는 처음 방문할 때 항상 최단으로 방문한다.
    - 그러나 가중치가 부여된 그래프에서는 BFS 역시 안된다.
      - 간선마다 거리가 다를 때는 판단 할 수가 없다.

![image-20220225165845750](C:\Users\qqq59\AppData\Roaming\Typora\typora-user-images\image-20220225165845750.png)



# BFS 활용법

1. 한 배열 내에서 여러 시작점을 동시에 탐색해야 할 경우

   배열이 아래와 같을 때 [0, 0] 좌표와 [4, 5] 좌표를 동시에 탐색해야 한다면

   ```
   1 -1 0 0 0 0 
   0 -1 0 0 0 0
   0 0 0 0 -1 0
   0 0 0 0 -1 1
   ```

    for 문을 통해 `queue`에 인자가 1인 좌표들을 모두 `append` 해 주고

   맨 앞 queue의 인자를 매개변수로 하는 BFS를 실행해서 탐색시키면 배열에서 추가한 좌표들 부터 탐색하므로 동시에 좌표를 탐색하는 모양이 된다.

   이 때 pop을 하면 맨 앞인자가 삭제되므로 queue.[0]을 사용하면 된다.

   

2. BFS에서 깊이 체크하기

   ```python
   def BFS(r, c):
       visited[r][c] = 1
   
       while q:
           r, c = q.popleft()
           for k in range(4):
               nr, nc = r + dr[k], c + dc[k]
               if 0 <= nr < N and 0 <= nc < M:
                   if tomato[nr][nc] == 0 and not visited[nr][nc]:
                       q.append((nr, nc))
                       # BFS의 깊이가 깊어질 때 마다 체크해줘야하므로
                       tomato[nr][nc] = tomato[r][c] + 1
                       # 방문 체크
                       visited[nr][nc] = 1
   ```

   

