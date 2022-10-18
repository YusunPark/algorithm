from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    moving = deque()
    moving_time = deque()

    time = 0
    while(truck or moving_time):
        if truck and sum(moving) + truck[0] <= weight:
            moving.append(truck.popleft())
            moving_time.append(bridge_length)
        
        for _ in range(len(moving_time)):
            moving_time.append(moving_time.popleft() - 1)
        if moving_time[0] == 0:
            moving_time.popleft()
            moving.popleft()
        time += 1
    
    return time + 1