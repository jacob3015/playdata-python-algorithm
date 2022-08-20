import heapq

def double_priority_queue(operations):
    """
    주어진 연산 문자열 operations를 수행한 결과 리스트를 반환한다.
    
    [parameter]
        operations :list - 명령어가 나열된 문자열 리스트
        
    [return]
        list - 명령어들을 수행한 결과 리스트
    
    [example]
        operations :list - ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
        return :list - [333, -45]
    """
    
    queue = []
    answer = [0, 0]
    
    for oper in operations:
        command, value = oper.split(' ')
        value = int(value)
        
        if command == 'I':
            heapq.heappush(queue, value)
        else:
            if not queue:
                continue
            if value < 0:
                heapq.heappop(queue)
            else:
                # nlargest(n, heap) : heap의 원소 중 가장 큰순으로 n개의 원소를 뽑아 내림차순으로 정렬한 리스트 반환
                queue = heapq.nlargest(len(queue), queue)[1:][::-1]

    if queue:
        if len(queue) == 1:
            answer[0], answer[1] = queue[0], queue[0]
        else:
            answer[0] = heapq.nlargest(1, queue)[0]
            answer[1] = heapq.heappop(queue)
    
    return answer