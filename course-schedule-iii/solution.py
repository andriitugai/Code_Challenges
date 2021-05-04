import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        pq = []
        time = 0

        for d, l in courses:
            if time + d <= l:
                heapq.heappush(pq, -d)
                time += d
            elif pq and -pq[0] > d:
                time += (d + heapq.heappop(pq))
                heapq.heappush(pq, -d)

        return len(pq)