class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        if counter.most_common(1)[0][1] * 2 > len(s) + 1:
            return ""

        res = []
        heap = []

        heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            # res.append(char1)
            # res.append(char2)
            res.extend([char1, char2])

            if count1 + 1 != 0:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1 != 0:
                heapq.heappush(heap, (count2 + 1, char2))

        if heap:
            res.append(heap[0][1])

        return "".join(res)
