"""
1부터 n까지 번호가 붙여진 n개의 가방이 있다. 각 가방은 다른 가방에 넣을 수 있으며, 다른 가방에 들어간 가방 역시 다른 가방을 넣고 있을 수 있다. 문제의 명확성을 위해 가방 i가 가방 j의 안에 있다는 것은 가방 i가 가방 j에 직접적으로 들어있음을 의미한다.예를 들어서, 가방 2가 가방 1 안에 있고, 가방 3이 가방 2 안에 있으면, 가방 3은 가방 2 안에 있지만 가방 1 안에 있지는 않다.

모든 가방은 처음에 다 빈 채로 바닥에 놓여 있다. 우리는 다음에 나열되는 것들 중 하나의 행동을 각각 단계적으로 취할 것이다.PUT i INSIDE j - 가방 i를 가방 j안에 넣는다. 이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여있어야 한다.SET i LOOSE - 가방 i안에 있는 모든 가방을 다시 꺼내서 바닥에 놓는다. 이 행동을 취하기 위해서는 가방 i는 반드시 바닥에 놓여 있어야 한다.

SWAP i WITH j - 가방 i와 가방 j의 내용물을 서로 바꾼다 (다시 말하면, 가방 i의 모든 내용물을 꺼내서 가방 j에 넣고, 가방 j의 모든 내용물을 꺼내서 가방 i에 넣는다).

이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여 있어야 한다.가방들이 놓여진 마지막 상태에서 어떤 가방도 자기보다 더 작은 번호의 가방 안에 들어가 있지 않을 때, 이 상태를 적절하다고 말한다.

주어진 가방의 개수 **int n**과 취할 행동의 단계 **vector<string> actions**를 이용하여 마지막 상태가 적절한지 판단하여라. 만약 적절하다면 마지막 상태에 바닥에 놓인 가방의 개수를 반환하여라. 적절하지 않거나 어느 단계의 행동이 유효하지 않다면 -1을 반환하여라.
"""


class Solution:
    def solution(self, n, actions):
        bags = [[] for _ in range(n + 1)]
        check = [1] * (n + 1)
        for action in actions:
            action = action.split()

            if action[0] == "SET":
                idx = int(action[1])
                if not check[idx]:
                    return -1

                for bag in bags[idx]:
                    check[bag] = 1
                bags[idx] = []

            elif action[0] == "PUT":
                x, y = int(action[1]), int(action[3])
                if not check[x] or not check[y]:
                    return -1

                bags[y].append(x)
                check[x] = 0

            elif action[0] == "SWAP":
                x, y = int(action[1]), int(action[3])
                if not check[x] or not check[y]:
                    return -1

                bags[x], bags[y] = bags[y], bags[x]

        for idx in range(1, n + 1):
            if bags[idx] and max(bags[idx]) > idx:
                return -1

        return sum(check[1:])

