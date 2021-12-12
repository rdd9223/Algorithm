# 다리를 지나는 트럭
# deque를 활용한 풀이
# sum을 그냥 사용했다가 시간초과 당했음. sum도 시간을 많이 먹는다.

from collections import deque


def solution(bridge_length, weight, truck_weights):
    """
    bridge_length개의 트럭까지 weight만큼만 올라갈 수 있음.
    트럭은 매초 1초에 length를 1씩 지나감
    """
    answer = 0

    wait_queue = deque(truck_weights)
    on_bridge_queue = deque([0 for _ in range(bridge_length)])
    on_bridge_weight = 0

    while not (not wait_queue and on_bridge_queue.count(0) == bridge_length):
        answer += 1
        out_truck = on_bridge_queue.popleft()
        on_bridge_weight -= out_truck

        if wait_queue and on_bridge_weight + wait_queue[0] <= weight and len(on_bridge_queue):
            new_truck = wait_queue.popleft()
            on_bridge_queue.append(new_truck)
            on_bridge_weight += new_truck
        else:
            on_bridge_queue.append(0)

    return answer
