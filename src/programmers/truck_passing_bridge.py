from collections import deque

def truck_passing_bridge(bridge_length, weight, truck_weights):
    """
    시작 시간: 14:47
    종료 시간: 15:35
    걸린 시간: 48분

    결과: 풀이 방법은 맞았으나 하나의 테스트 케이스에 대해 시간 초과 나옴
    원인: 현재 다리에 올라간 트럭들의 무게 합을 sum(bridge)으로 구해 시간 초과가 나온 것으로 보임
    해결: 다리에 올라간 트럭들의 무게 합을 나타내는 변수를 사용함

    원인 분석:
        while문 내부에서 sum() 함수 사용 시 시간복잡도 = O(n^2)
        따라서, 5번 테스트 케이스에서 시간 초과가 난것으로 보임

    해결 분석:
        sum() 함수를 사용하지 않고 변수 사용 시 시간복잡도 = O(n)

    정리:
        n번 반복하는 반복문 내부에서 자료구조를 완전탐색하는 내장함수 사용 시 시간복잡도가 O(n^2)가 됨
        따라서, 시간복잡도를 따져보고 사용 가능한 경우에만 사용해야함

    다리에 올라갈 수 있는 트럭 수: 2
    다리가 견딜 수 있는 하중: 10
    대기중인 트럭들: [7, 4, 5, 6]

    1s: candidate = 7, queue = [4, 5, 6] -> bridge = [7]
    2s: candidate = 4, queue = [5, 6] -> bridge = [7, 0], queue = [4, 5, 6]
    3s: bridge = [0] -> candidate = 4, queue = [5, 6] -> bridge = [0, 4]
    4s: bridge = [4] -> candidate = 5, queue = [6] -> bridge = [4, 5]
    5s: bridge = [5] -> candidate = 6, queue = [] -> bridge = [5, 0], queue = [6]
    6s: bridge = [0] -> candidate = 6, queue = [] -> bridge = [6]

    answer = time + bridge_length

    """

    bridge = deque()
    queue = deque(truck_weights)
    time = 0
    bridge_weight = 0

    while queue:
        time += 1

        if bridge_length - len(bridge) == 0:
            bridge_weight -= bridge.popleft()

        candidate = queue.popleft()
        
        if bridge_length - len(bridge) > 0 and bridge_weight + candidate <= weight:
            bridge.append(candidate)
            bridge_weight += candidate
        else:
            bridge.append(0)
            queue.appendleft(candidate)

    return time + bridge_length


print(truck_passing_bridge(2, 10, [7, 4, 5, 6]))