import array
import bisect
import heapq
from collections import deque

prices = array.array('d',[102.5, 98.0, 105.3, 97.5, 110.0, 95.0, 103.2, 99.8, 107.1, 101.4])

lastfive = deque(maxlen=5)

historyrank = list()

for i in range(len(prices)):

    print("New price:", prices[i])

    lastfive.append(prices[i])

    position = bisect.bisect(historyrank, prices[i])
    historyrank.insert(position, prices[i])

    print("Rolling window (last 5):", lastfive)

    print("Position in the history: position", position+1, "out of", i+1)
    
history = list(prices)
history.sort()

new = 105.4

pos = bisect.bisect(history, new)
history.insert(pos, new)

heapq.heapify(history)
smallthree = heapq.nsmallest(3, history)


print("Top 3 smallest prices in history:", smallthree)
