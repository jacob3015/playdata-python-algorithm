from collections import deque

def farthest_node(n, vertex):
    """
    시작 시간: 15:50
    종료 시간: 16:30
    걸린 시간: 40분

    1번 노드에서 출발해 각 노드에 도달하는데 필요한 최단거리를 구하면 될 듯?

    결과: 다익스트라 알고리즘을 이용해 시작 노드에서 출발해 각 노드에 도달하는데 필요한 최단 거리를 구함
    정리:
        간선의 길이가 1로 동일하기 때문에 우선순위 큐가 아닌 큐를 사용해 해결
        간선의 길이가 서로 다르다면 우선 순위 큐를 사용해 노드와 연결된 간선 중 최단 거리를 구하는 것이 유리함
    """

    INF = 1e10

    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    queue = deque()

    graph = [[] for _ in range(n+1)]

    for edge in vertex:
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)

    start = 1
    distance[start] = 0
    queue.append(start)

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            for conn in graph[node]:
                new_distance = distance[node] + 1
                if distance[conn] > new_distance:
                    distance[conn] = new_distance
                queue.append(conn)

    answer_distance = max(distance[1:])

    return distance.count(answer_distance)

print(farthest_node(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))