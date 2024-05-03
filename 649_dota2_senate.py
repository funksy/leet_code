from collections import deque

def predictPartyVictory(senate):
    rad = deque([])
    dire = deque([])
    for i in range(len(senate)):
        if senate[i] == 'R':
            rad.append(i)
        else:
            dire.append(i)
    idx = len(senate)
    while rad and dire:
        if rad[0] < dire[0]:
            rad.append(idx)
        else:
            dire.append(idx)
        idx += 1
        rad.popleft()
        dire.popleft()
    if rad:
        return "Radiant"
    else:
        return "Dire"


print(predictPartyVictory("RDD"))