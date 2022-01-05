from collections import deque


def solution(prices):
    seconds = []
    prices = deque(prices)
    while prices:
        counter = 0
        price = prices.popleft()

        for next_price in prices:
            counter += 1
            if price > next_price:
                break
        seconds.append(counter)
    return seconds


res = solution([1, 2, 3, 2, 3])
print(res)
