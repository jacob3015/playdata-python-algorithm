def life_boat(people, limit):
    """
    모든 사람을 구출하기 위해 필요한 최소한의 구명보트 개수를 구해 반환한다
    
    [parameter]
        people :list - 사람들의 몸무게
        limit :int - 구명보트 무게 제한
        
    [return]
        int - 필요한 최소한의 구명보트 개수
        
    [example]
        people - [70, 50, 80, 50]
        limit - 100
        return - 3
    """
    answer = 0
    
    people.sort()
    
    start, end = 0, len(people) - 1
    
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        
    return answer