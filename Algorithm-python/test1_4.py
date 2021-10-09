"""
- 문제
당신은 새 물건을 판매하기에 앞서 어떻게 하면 매출을 극대화할 수 있는지 알고 싶다.
물건의 최적의 가격을 정하는 것도 여러 전략 중 하나이다.
당신은 잠재적 고객들이 지출할 수 있는 제일 높은 가격을 적은 고객 목록을 만들었다.
당신은 또한 각 고객들에게 물건을 배송하기 위해 얼마의 비용이 필요한지 알고 있다.
배송 비용은 당신이 모두 부담해야되기 때문에 배송 비용이 너무 비싸다면 그 고객에게는 물건을 팔지 않을 수도 있다.
주어진 정수배열 **price** 과  **cost** 에는 각각 고객 i가 지출할 수 있는 제일 높은 가격과 배송 비용이 담겨 있다.
매출을 극대화할 수 있는 물건의 가격을 반환하여라.
최적의 가격이 2가지 이상 존재한다면 더 작은 가격을 리턴하시오.
이윤을 남길 수 없다면 0을 리턴하시오.
"""


class Solution:
    def solution(self, price, cost):
        arr = []
        for i in range(len(price)):
            if (price[i] - cost[i] > 0):
                arr.append((price[i], cost[i]))
        arr = sorted(arr, key=lambda arr: arr[0])

        maxProfit = 0
        maxProfitPrice = 0

        for i in range(len(arr)):
            salePrice = arr[i][0]
            sum = 0

            for x in arr[i:]:
                if salePrice - x[1] <= 0:
                    continue
                sum += (salePrice - x[1])

            if sum > maxProfit:
                maxProfit = sum
                maxProfitPrice = salePrice

        return maxProfitPrice