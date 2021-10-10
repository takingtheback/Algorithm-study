"""
- 문제

    재미있는 게임을 해보자.

    "is there anybody out there"이라는 문자열을 빈칸으로 구분한 각 단어들의 길이를 써보면 2, 5, 7, 3, 5이 된다.

    '1'부터 '9'로만 이루어진 문자열  **number**와 문자열 배열 **dictionary** 이 주어진다.

    우리는 이 두개의 데이터를 가지고 문장을 만들어 내야 한다.

    number의 각 요소 number[i]는 i번째로 올 단어의 길이를 나타낸다.

    dictionary의 각 요소는 단어를 나타낸다.

    예를들어 입력이 아래와 같다고 가정해보면

    number = "25735"

    dictionary = ["is","there","anybody","out","there"]

    "is there anybody out there"이 리턴값이 된다. 만약 같은 길이의 단어를 골라야 된다면, 알파벳 순서로 먼저 있는것을 우선하여 고른다.

    이때, 주어지는 number와 dictionary에 따라 올바른 답을 반환하시오.
"""
class Solution:
    def solution(self, code, message):
        code = list(code)
        answer = ""

        if message.isdigit():
            message = [int(message[i:i + 2]) for i in range(0, len(message), 2)]
            for i in message:
                answer += code[i - 1]
        else:
            for i in message:
                answer += str(code.index(i) + 1).rjust(2, '0')

        return answer