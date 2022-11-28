def life_boat(people, limit):
    """
    시작 시간: 14:50
    종료 시간: 15:28
    걸린 시간: 38분

    풀이:
        오름차순 정렬 후 무게가 많이 나가는 사람들부터 배에 태워 보낸다.
        무게가 많이 나가는 사람과 적게 나가는 사람의 무게 합이 무게 제한보다 작거나 같으면,
        무게가 적게 나가는 사람도 같이 태워 보낸다.
        모든 사람들 배에 태워 내보낼 때까지 위 과정을 반복한다.
    """
    answer = 0

    start, end = 0, len(people) - 1

    people.sort()

    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return answer

print(life_boat([70, 50, 80, 50], 100))