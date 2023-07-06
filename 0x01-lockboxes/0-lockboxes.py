def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    keys = [0]
    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.append(key)

    return all(unlocked_boxes)

