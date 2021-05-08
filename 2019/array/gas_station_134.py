class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        remain = 0; start = 0
        sum = 0
        for i in range(n):
            remain += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if remain < 0:
                start = i + 1
                remain = 0
        if sum >= 0: return start
        else: return -1

