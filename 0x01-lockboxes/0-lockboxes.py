from collections import deque

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = set()
    queue = deque([0])  # Start with box 0

    while queue:
        current_box = queue.popleft()
        visited.add(current_box)

        # Check the keys in the current box
        for key in boxes[current_box]:
            if key not in visited and key < num_boxes:
                queue.append(key)

    return len(visited) == num_boxes

