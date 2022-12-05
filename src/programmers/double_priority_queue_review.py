import heapq

def double_priority_queue(operations):
    """
    시작 시간: 16:38
    종료 시간: 17:52
    걸린 시간: 74분

    정리:
         heapq.heapify()를 활용해 큐에서 최댓값을 삭제함
         heapq.heappop()를 활용해 큐에서 최솟값을 삭제함
    """
    queue = []

    for operation in operations:
        operation = operation.split()
        oper, value = operation[0], int(operation[1])

        if oper == "I":
            queue.append(value)
        else:
            if value > 0:
                delete_max(queue)
            else:
                delete_min(queue)

    if queue:
        return [max(queue), min(queue)]
    else:
        return [0, 0]

def delete_max(queue):

    if queue:
        heapq.heapify(queue)
        queue.pop()

def delete_min(queue):

    if queue:
        heapq.heappop(queue)

print(double_priority_queue(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))