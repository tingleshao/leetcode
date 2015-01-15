# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
         
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
      intervals = sorted(intervals, key = lambda x: x.start)
      if intervals == []:
        return [newInterval]
      res = []
      newInt = []
      if newInterval.end < intervals[0].start:
        res = list(intervals)
        res.insert(0,newInterval)
        return res
      for i in xrange(len(intervals)):
        if intervals[i].end >= newInterval.start:
          newInt.append(min(newInterval.start,intervals[i].end))
        elif intervals[i].end >= newInterval.end:
          if newInt == []:
            newInt.append(max(newInterval.start,intervals[i].start))
            res.append(Interval(newInt[0],newInt[1]))
        elif intervals[i].end <= newInterval.end:
          continue
        else:
          res.append(intervals[i])
      if newInt == []:
        res.append(newInterval)
      return res
            
        
                      
def main():
    s = Solution()
    i1 = Interval(5,7)
    i2 = Interval(1,5)
    i3 = Interval(2,3)
    
    print s.insert([],i1)
    xx = s.insert([i2],i3)
    print xx[0].start, xx[0].end
    
    
if __name__ == "__main__":
    main()