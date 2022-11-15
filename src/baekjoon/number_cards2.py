from collections import Counter

def number_cards2(cards_size, cards, numbers_size, numbers):
    """
    시작 시간: 16:35
    종료 시간: 16:49
    걸린 시간: 14분

    결과: 양수를 저장하는 list와 음수를 저장하는 list를 사용해서 counting sort로 문제를 해결해 보았지만 메모리 초과 나옴
    원인: list의 크기가 커서 메모리 초과가 난 것으로 보임
    해결: collections.Counter()를 사용해 collections 자료구조 내 각 원소의 개수를 dictionary로 구함

    해결 분석:
        원인에 대해 딱 맞는 해결책은 아니지만 다른 방법으로 문제를 해결함
    """

    cards_number = Counter(cards)

    answer = []

    for number in numbers:
        if number in cards_number:
            answer.append(cards_number.get(number))
        else:
            answer.append(0)
    
    for result in answer:
        print(result, end=" ")

number_cards2(10, [6, 3, 2, 10, 10, 10, -10, -10, 7, 3], 8, [10, 9, -5, 2, 3, 4, 5, -10])