def n_representation(N, number):
    """
    시작 시간: 16:40
    종료 시간: 19:00
    걸린 시간: 140분

    결과: 몇몇 테스트 케이스를 틀림

    원인: 
        바로 전 연산 결과와 N 간의 사칙연산만을 수행해 K번째 집합을 구성함
        또한, 피연산자의 순서에 따라 뺼셈과 나눗셈은 결과가 달라진다는 것을 간과함
        
    해결: DP를 이용해 이전 연산 결과 간의 사칙연산을 수행해 n번째 집합을 구성함
    """
    if N == number:
        return 1

    memo = [set() for _ in range(9)]
    memo[1].add(N)

    for now in range(2, 9):
        memo[now].add(int(str(N) * now))
        for post in range(1, now):
            for value1 in list(memo[post]):
                for value2 in list(memo[now - post]):
                    memo[now].update([value1 + value2, value1 * value2])
                    memo[now].update([value1 - value2, value2 - value1])
                    if value1 != 0:
                        memo[now].add(value2 // value1)
                    if value2 != 0:
                        memo[now].add(value1 // value2)
        if number in memo[now]:
            return now

    return -1


print(n_representation(5, 31168))