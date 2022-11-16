def secret_map(n, arr1, arr2):
    """
    시작 시간: 16:49
    종료 시간: 17:15
    걸린 시간: 26분

    해결:
        format(value, format_spec) 내장 함수를 사용해 정수를 이진수 문자열로 변환함
        value에는 정수값을, format_spec에는 이진수 문자열을 뜻하는 0b를 제외하고 길이는 n으로 고정하도록 하여 변환함
    """

    answer = []

    for (line1, line2) in zip(arr1, arr2):
        bin_str1 = format(line1, f"0{n}b")
        bin_str2 = format(line2, f"0{n}b")

        new_line = ""

        for (str1, str2) in zip(bin_str1, bin_str2):
            if str1 == "0" and str2 == "0":
                new_line += " "
            else:
                new_line += "#"

        answer.append(new_line)


    return answer

print(secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))