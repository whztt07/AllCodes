
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        sumDuration = 0
        lastEnd = 0        
        for v in timeSeries:
            dValue = duration
            if v < lastEnd:
                dValue += v - lastEnd
            
            sumDuration += dValue
            lastEnd = v + duration

        return sumDuration


# Test Case
import unittest
class SolutionTest(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.findPoisonedDuration([1,4],2),4)
        self.assertEqual(s.findPoisonedDuration([1,2],2),3)
        self.assertEqual(s.findPoisonedDuration([1,4,5,6,10,14,15,34],2),13)

if __name__ == '__main__':    
    unittest.main()
    