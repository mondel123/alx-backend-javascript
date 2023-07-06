def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is initially unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)

