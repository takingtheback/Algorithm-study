"""
당신은 학교에서 집까지 도시를 거쳐 걸어가고 있다.
도시는 무한히 크며 모든 X값에는 수직 도로가 놓여있고 모든 Y에는 수평 도로가 놓여있다.
당신은 현재 (0, 0)에 있으며 (X, Y)에 있는 집에 가려고 한다. 집까지 가는 방법에는 두가지가 있다:
수평 혹은 수직으로 인접한 교차로를 거쳐 ( walkTime 초가 걸린다) 도로를 따라 걷는 것과
몰래 대각선으로 건너 ( sneakTime 초가 걸린다) 반대쪽 모서리로 가는 방법이 있다.
이미지에 나와있는 것처럼 걷거나 대각선을 가로지르는 8가지 방향 어느쪽으로도 가는 것이 가능하다 (예제 2번 참고).
![](../../../Downloads/test2_1.png)
"""


class Solution:
    def solution(self, X, Y, walkTime, sneakTime):

        # 수평, 수직 걷기 시간
        walk = (X + Y) * walkTime

        # 수평 + 수직 거리가 짝수이고 대각선으로 쭉 갈 수 있는 경우
        # 정사각형 같은 모양

        if (X + Y) % 2 == 0:
            walk_s = max(X, Y) * sneakTime

        # 홀수면 대각선으로 쭉 가고 마지막 한칸만 수평 또는 수직으로
        # 직사각형 같은 모양

        if (X + Y) % 2 == 1:
            walk_s = (max(X, Y) - 1) * sneakTime + walkTime

        # 수평, 수직 + 대각선의 경우
        # 복합
        walk_complex = (min(X, Y) * sneakTime) + ((max(X, Y) - min(X, Y)) * walkTime)

        # 셋 중에 가장 짧은 시간
        result = min(min(walk, walk_s), walk_complex)

        return result