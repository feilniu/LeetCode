import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        Itinerary = []
        if tickets:
            Routes = collections.defaultdict(list)
            for a, b in sorted(tickets, reverse = True):
                Routes[a] += b,
            Stack = ['JFK']
            while Stack:
                while Routes[Stack[-1]]:
                    Stack += Routes[Stack[-1]].pop(),
                Itinerary += Stack.pop(),
        return Itinerary[::-1]

testCases = [
        [[], []],
        [[["JFK", "PVU"]], ["JFK", "PVU"]],
        [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]],
        [[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"]],
        [[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]], ["JFK","NRT","JFK","KUL"]],
        [[["JFK","A"],["A","B"],["B","A"],["A","C"],["A","D"],["D","E"],["E","A"]], ["JFK","A","B","A","D","E","A","C"]],
        [[["JFK","A"],["A","B"],["B","C"],["A","D"],["D","E"],["E","A"]], ["JFK","A","D","E","A","B","C"]],
        [[["JFK","A"],["A","B"],["B","C"],["C","E"],["A","D"],["D","E"],["E","A"]], ["JFK","A","B","C","E","A","D","E"]],
        [[["JFK","E"],["E","D"],["D","C"],["C","E"],["C","A"],["E","D"],["D","C"]], ["JFK","E","D","C","E","D","C","A"]],
        ]
passedCount = 0
s = Solution()
for tc in testCases:
    result = s.findItinerary(*tc[:-1])
    passed = result == tc[-1]
    if passed:
        passedCount += 1
    else:
        print(tc, result, passed)
print('{}/{} test cases passed.'.format(passedCount, len(testCases)))

