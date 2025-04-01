'''
// Time Complexity :
# Problem 1 - O(V+E) V - vertices, E - edges of the graph
# Problem 2 - O(1) for each operation - O(n) to iterate the entire list
// Space Complexity :
# Problem 1 - O(n) n - no. of people
# Problem 2 - O(n) worst case if we check all the elements
// Did this code successfully run on Leetcode :
# Yes the code ran successfully.

// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
'''
## Problem 1 - Best Time to Buy and Sell Stock II
# Initializa the first day stock price in a variable along with profit variable
# Iterate over the prices array and calculate the difference only when the stock price is greater than 
# previous price to gain profit
# Since we can buy the share again after selling it the profit can be cumulatively calculated
# Return the profit calculated else return the profit as '0'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stock_price = prices[0]
        n = len(prices)
        profit = 0
        for i in range(1,n):
            if stock_price < prices[i]:
                profit += prices[i] - stock_price
            stock_price = prices[i]
        return profit

## Problem 2 - Peeking Iterator
# Initializa the iterator and store the first element in result if the hasNext() returns a value
# Peek = Return the current element in result
# Next = Store the current element in a temp variable, if next element exists then return temp else None
# hasNext = Check if the next elements exists return 'True' else 'False'.

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        self.result = self.itr.next() if self.itr.hasNext() else None        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.result
        

    def next(self):
        """
        :rtype: int
        """
        temp = self.result
        self.result = self.itr.next() if self.itr.hasNext() else None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.result is not None      

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].