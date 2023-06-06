from sys import stdin
class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    n = len(intervals)
    ans = [intervals[0]]
    for interval in intervals[1:]:
        if interval.start <= ans[-1].end:
            ans[-1].end = max(ans[-1].end,interval.end)
            ans[-1].start = min(ans[-1].start,interval.start)
        else:
            ans.append(interval)
    return ans


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
