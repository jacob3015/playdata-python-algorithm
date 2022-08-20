import heapq

def scoville_score(scoville, K):
    """
    모든 음식이 스코빌 지수 K 이상이 되는데 필요한 섞는 횟수를 구해 반환한다.
    모든 음식이 K 이상의 스코빌 지수가 불가능한 경우 -1을 반환한다.
    
    [parameter]
        scoville :list - 음식들의 스코빌 지수
        K :int - 스코빌 지수 기준점
        
    [return]
        int - 모든 음식들의 스코빌 지수가 K 이상이 되는데 필요한 섞기 횟수
        
    [example]
        scoville_score :list - [1, 2, 3, 9, 10, 12]
        K :int - 7
        return :int - 2
    """
    
    queue = []
    answer = 0
    
    for score in scoville:
        heapq.heappush(queue, score)
        
    while len(queue) > 1:
        first = heapq.heappop(queue)
        
        if first >= K:
            break
            
        second = heapq.heappop(queue)
        heapq.heappush(queue, first + (second * 2))
        answer += 1
        
    if heapq.heappop(queue) < K:
        answer = -1
    
    return answer
    