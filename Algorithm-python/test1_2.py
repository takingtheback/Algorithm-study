"""
행운의 번호는 2*n 자릿수를 가진 숫자인데, 왼쪽에서부터 n 개의 숫자의 합이 오른쪽에서부터 n 개의 숫자의 합과 같다.

당신에게 0을 제외한 숫자로만 이루어진 문자열 **s**가 주어진다. 이 문자열의 부분문자열 중 가장 긴 행운의 번호의 길이를 구하시오. 만약 행운의 번호가 없다면 0을 반환하시오.
"""

class Solution:
    def solution(self, s):
        s = None

        # s의 길이 만큼 반복문을 돌린다.
        # 돌리면서 조건문을 통해 부분문자열이 중복이 안될때 그때의 숫자를 얻어 그 수만큼 더해준다.
        for i in range(len(s)):
            if s[i:] == s[i:][::-1]:
                print(len(s) + i)
                final = len(s) + i
                break
        return final
