class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
      left, right = 0, len(num)-1
      while (right-left) > 1:
        mid = left+(right-left) / 2
        if num[mid] > num[left] and num[mid] > num[right]:
          left = mid 
        elif num[mid] == num[left]:
          left += 1
        else:
          right = mid
      return min(num[left],num[right])
      