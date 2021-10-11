"""
- 문제

    행운의 번호는 2*n 자릿수를 가진 숫자인데, 왼쪽에서부터 n 개의 숫자의 합이 오른쪽에서부터 n 개의 숫자의 합과 같다.

    당신에게 0을 제외한 숫자로만 이루어진 문자열 **s**가 주어진다. 이 문자열의 부분문자열 중 가장 긴 행운의 번호의 길이를 구하시오. 만약 행운의 번호가 없다면 0을 반환하시오.
"""


class Solution:
    def solution(self, instructions):
        result = 0
        for i in range(len(instructions)):
            if instructions[i] == 'LEFT':
                result -= 90
            elif instructions[i] == 'RIGHT':
                result += 90
            elif instructions[i] == 'TURN AROUND':
                result += 180

            elif instructions[i] != 'TURN AROUND' and len(instructions[i]) > 5:
                if instructions[i][:4] == 'LEFT':
                    result -= int(instructions[i][4:])

                elif instructions[i][:5] == 'RIGHT':
                    result += int(instructions[i][5:])

            elif instructions[i] == 'HALT':
                break

        while result > 360:
            result -= 360
            if result < 0:
                break

        while result < 0:
            result += 360

        if result == 360:
            result = 0

        return result