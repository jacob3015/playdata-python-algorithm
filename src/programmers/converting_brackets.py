from collections import deque

def converting_brackets(brackets):
    """
    시작 시간: 16:16
    종료 시간: 17:18
    걸린 시간: 62분

    결과:
        재귀함수 문제지만 문제 내 풀이 방법이 나와 있어 구현 문제에 가까움
        문제에 나와있는 풀이 방법 그래도 구현해 한번에 해결함

    정리:
        한번에 해결하기는 했지만 validate() 함수 구현에 시간이 오래 걸림
    """
    if not brackets:
        return brackets
    
    brackets1, brackets2 = divide(brackets)

    if validate(brackets1):
        return brackets1 + converting_brackets(brackets2)
    else:
        new_brackets = "("
        new_brackets += converting_brackets(brackets2)
        new_brackets += ")"
        new_brackets += flip(brackets1[1:len(brackets1)-1])
        return new_brackets

def divide(string):

    right = 0
    left = 0

    for bracket in string:
        if bracket == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break

    size = left + right

    return string[0:size], string[size:]

def validate(string):

    result = True

    value = deque(string)
    stack = []

    while value:
        next = value.popleft()
        if next == "(":
            stack.append(next)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return result

def flip(string):

    new_string = ""

    for bracket in string:
        if bracket == "(":
            new_string += ")"
        else:
            new_string += "("

    return new_string

print(converting_brackets("()))((()"))