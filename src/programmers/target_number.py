def target_number(numbers, target):
    """
    시작 시간: 15:08
    종료 시간: 16:21
    걸린 시간: 73분

    결과: 
        해결 과정에서 DFS를 활용하기 위해 그래프를 구성하기 위해 고민했으나
        굳이 그래프를 구성하고 값을 탐색하며 값을 계산할 필요가 없음을 알게됨

    해결:
        계산한 결과를 리스트에 메모해가며 최종 결과 리스트를 구하고,
        결과 리스트에서 타겟 갯수를 찾는 방법으로 해결함
    
    결과 분석: 문제 풀이 방식을 전형적인 DFS 탐색 방법으로 제한해 생각함

    해결 분석: 시간복잡도가 O(n^2) 으로 효율적이지 못하다고 생각함

    정리:
        좀 더 유연하게 문제 풀이 방식에 접근할 필요가 있으며,
        좀 더 효율적인 알고리즘을 생각해볼 필요가 있음
    """
    answer = 0

    root = [0]

    for number in numbers:
        leaf = []
        for value in root:
            leaf.append(value + number)
            leaf.append(value - number)
        root = leaf

    answer = root.count(target)

    return answer


print(target_number([1, 1, 1, 1, 1], 3))