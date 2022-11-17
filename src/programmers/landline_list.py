from collections import deque

def landline_list(phone_book):
    """
    시작 시간: 14:46
    종료 시간: 15:46
    걸린 시간: 60분

    결과: 정확성 테스트는 통과했으나, 효율성 테스트에서 시간초과 나옴
    원인: 사용한 알고리즘의 시간복잡도 O(n^2)
    해결:
        정수 문자열을 정렬하면, 접두사와 접두사가 붙은 문자열이 앞 뒤로 정렬된다는 것을 이용함
        앞 뒤 문자열 비교를 위해 deque.rotate() 를 사용해서 앞 뒤 문자열을 비교할 수 있도록 함

    정리:
        테스트 케이스가 100만개로 시간복잡도 O(n^2) 알고리즘으로 풀면 안된다는 것을 알았지만 다른 풀이가 떠오르지 않음
        많은 문제를 풀어볼 필요가 있음
    """
    answer = True

    phone_book = sorted(phone_book)
    rotated_book = deque(phone_book)
    rotated_book.rotate(-1)

    for number1, number2 in zip(phone_book, rotated_book):
        if number2.startswith(number1):
            return False
    
    return answer

print(landline_list(["119", "456", "11955"]))