class Solution(object):
    def maxProfit(self, prices):
        minsofar = 10000
        maxprofit = 0
        for p in prices:
            if p<minsofar:
                minsofar = p
            maxprofit = max(maxprofit,p-minsofar)  
        return maxprofit
        